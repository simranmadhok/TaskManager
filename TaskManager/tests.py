from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from TaskManager.forms import SignUpForm, TaskCommentsForm, TaskForm
from TaskManager.models import Task, TaskComments


class LoginTestCase(TestCase):
    """
        Test case for user to log in with valid and invalid credentials
    """

    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get('/tm/login/')
        self.assertEqual(response.status_code, 200)
        self.client.login(username='user1', password="pass@1234")
        response = self.client.get(reverse('task_list'), follow=True)
        self.assertEqual(response.status_code, 200)

class LogoutTestCase(TestCase):
    """
        Test case for user to log out
    """

    def setUp(self):
        self.client = Client()

    def test_logout_admin_civis(self):
        self.client.login(username='user1', password="pass@1234")
        response = self.client.get(reverse('task_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class RegisterUserTestCase(TestCase):


    def test_get_register_user(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './TaskManager/signup.html')

    def test_invalid_email_register_user_form(self):
        data = {
            'username': 'user1',
            'password': 'lmnopz',
            'email': 'user@abc',
            'first_name': 'abc',
            'last_name': 'xyz'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './TaskManager/signup.html')
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_common_password_register_user_form(self):
        data = {
            'username': 'user1',
            'password1': '1234',
            'password2': '1234',
            'email': 'user@abc.com'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './TaskManager/signup.html')
        self.assertFormError(response, "form", "password2", "This password is too common.")

    def test_similar_password_register_user_form(self):
        data = {
            'username': 'user1',
            'password1': 'user1',
            'password2': 'user1',
            'email': 'user@abc.com'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './TaskManager/signup.html')
        self.assertFormError(response, "form", "password2", "The password is too similar to the username.")

    def test_numeric_password_register_user_form(self):
        data = {
            'username': 'user1',
            'password1': '98798798',
            'password2': '98798798',
            'email': 'user@abc.com'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, './TaskManager/signup.html')
        self.assertFormError(response, "form", "password2", "This password is entirely numeric.")

    def test_valid_register_user_form(self):
        data = {
            'username': 'user1',
            'password1': 'pass@1234',
            'password2': 'pass@1234',
            'email': 'user@abc.com'
        }
        response = self.client.post(reverse('signup'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('login'), follow=True)
        self.assertEqual(response.status_code, 200)

class TaskCreateTestCase(TestCase):
    """
        Test case for user to create a new task
    """

    def setUp(self):
        self.client = Client()
        self.client.login(username='user1', password="pass@1234")

    def test_get_create_task_form(self):
        response = self.client.get(reverse('task_list'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_valid_task_create_form(self):
        data = {
            'title': 'task 1',
            'priority': 'high',
            'date_due': '2020-11-02'
        }
        response = self.client.post(reverse('task_list'), data, follow=True)
        self.assertEqual(response.status_code, 200)

class TaskDeleteTestCase(TestCase):
    """
        Test case for user to delete a task
    """

    def setUp(self):
        user_obj = User.objects.create(username='user1', password='pass@1234')
        Task.objects.create(user=user_obj, title='task 1', priority='high', date_due='2020-11-02')
        Task.objects.create(user=user_obj, title='task 2', priority='medium', date_due='2020-11-03')
        Task.objects.create(user=user_obj, title='task 3', priority='low', date_due='2020-11-04')
        self.client = Client()
        self.client.login(username='user1', password="pass@1234")
        

    def test_delete_task(self):
        response = self.client.get(reverse('task_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        pk=1
        task = Task.objects.get(pk=pk)
        response = self.client.post(reverse('task_delete', kwargs={"pk": task.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
        task_obj = Task.objects.get(pk=pk)
        task_obj.delete()

class TaskUpdateTestCase(TestCase):
    """
        Test case for user to update task status
    """

    def setUp(self):
        user_obj = User.objects.create(username='user1', password='pass@1234')
        Task.objects.create(user=user_obj, title='task 1', priority='high', date_due='2020-11-02', completed=False)
        self.client = Client()
        self.client.login(username='user1', password="pass@1234")
        

    def test_delete_task(self):
        response = self.client.get(reverse('task_list'), follow=True)
        self.assertEqual(response.status_code, 200)
        pk=1
        task = Task.objects.get(pk=pk)
        response = self.client.post(reverse('task_completed', kwargs={"pk": task.pk}), follow=True)
        self.assertEqual(response.status_code, 200)
        task_obj = Task.objects.get(pk=pk)
        task_obj.completed = False

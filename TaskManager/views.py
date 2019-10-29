from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import SignUpForm, TaskCommentsForm, TaskForm
from .models import Task, TaskComments


class SignUpView(CreateView):
    model = User

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
        else:
            return render(request, './TaskManager/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, './TaskManager/signup.html', {'form': form})

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task

    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        task_list = Task.objects.filter(user=self.request.user)
        if task_form.is_valid():
            task_obj = task_form.save(commit=False)
            task_obj.user = self.request.user
            comment_obj = TaskComments.objects.create(comments='')
            comment_obj.save()
            task_obj.comment = comment_obj
            task_obj.save()
            task_form = TaskForm()
        return render(request, './TaskManager/tasks.html', {'task_form': task_form, 'task_list': task_list})

    def get(self, request, *args, **kwargs):
        task_form = TaskForm()
        task_list = Task.objects.filter(user=self.request.user)
        return render(request, './TaskManager/task_list.html', {'task_form': task_form, 'task_list': task_list})

@login_required
def task_delete(request, pk):
    if request.method=='POST':
        task_obj = Task.objects.get(pk=pk)
        task_obj.delete()
        task_list = Task.objects.filter(user=request.user)
        task_form = TaskForm()
        return render(request, './TaskManager/tasks.html', {'task_form': task_form, 'task_list': task_list})

@login_required
def task_completed(request, pk):
    if request.method=='POST':
        task_obj = Task.objects.get(pk=pk)
        if task_obj.completed == True:
            task_obj.completed = False
        elif task_obj.completed == False:
            task_obj.completed = True
        task_obj.save()
        task_list = Task.objects.filter(user=request.user)
        task_form = TaskForm()
        return render(request, './TaskManager/tasks.html', {'task_form': task_form, 'task_list': task_list})


class UpdateCommentView(LoginRequiredMixin, UpdateView):
    model = TaskComments
    success_url = reverse_lazy('task_list')

    def post(self, request, pk, *args, **kwargs):
        task_comment_obj = TaskComments.objects.get(pk=pk)
        task_comments_form = TaskCommentsForm(request.POST, request.FILES, instance=task_comment_obj)
        if task_comments_form.is_valid():
            task_comments_form.save()
            task_form = TaskForm()
            task_list = Task.objects.filter(user=self.request.user)
        return render(request, './TaskManager/task_list.html', {'task_form': task_form, 'task_list': task_list})

    def get(self, request, pk, *args, **kwargs):
        task_form = TaskForm()
        task_comment_obj = TaskComments.objects.get(pk=pk)
        task_comments_form = TaskCommentsForm(instance=task_comment_obj)
        task_list = Task.objects.filter(user=self.request.user)
        return render(request, './TaskManager/task_list.html', {'task_form': task_form, 'task_comments_form': task_comments_form, 'task_list': task_list, 'task_comment_obj': task_comment_obj})

import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Task, TaskComments


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class TaskForm(forms.ModelForm):
    PRIORITY = (
        ('high','high'),
        ('medium','medium'),
        ('low','low')
    )
    class Meta:
        model = Task
        fields = ('title', 'priority', 'date_due', 'comment')
        widgets = {
            'date_due': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'0000-00-00', 'type':'date'}),
        }

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Title', 'autofocus': 'autofocus'}), required=True)
    priority = forms.ChoiceField(widget=forms.RadioSelect, required=True, choices=PRIORITY)


class TaskCommentsForm(forms.ModelForm):
    class Meta:
        model = TaskComments
        fields = ('comments', 'attachment')
    
    attachment = forms.FileField(widget=forms.FileInput(), required=False)
    comments = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Enter comments', 'rows': 3}), required=False)

    # def save(self, *args, **kwargs):
    #     image_path = self.instance.attachment.name
    #     if os.path.isfile(image_path):
    #         os.remove(image_path)
    #     comment_instance = super(TaskCommentsForm, self).save(*args, **kwargs)
    #     return comment_instance
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
     path('logout/', LogoutView.as_view(template_name="TaskManager/login.html"), name='logout'),
     # ex: /tm/
     path('', LoginView.as_view(template_name="TaskManager/login.html"), name='login'),
     # ex: /tm/login/
     path('login/', LoginView.as_view(template_name="TaskManager/login.html"), name='login'),
     # ex: /tm/signup/
     path('signup/', views.SignUpView.as_view(), name='signup'),
     # ex: password_reset/
     path('password_reset/',
          PasswordResetView.as_view(template_name='TaskManager/password_reset_form.html'),
          name='password_reset'),
     # ex: password_reset_done/
     path('password_reset_done/',
          PasswordResetDoneView.as_view(template_name='TaskManager/password_reset_done.html'),
          name='password_reset_done'),
     # ex: reset/<uidb64>/<token>/
     path('reset/<uidb64>/<token>/',
          PasswordResetConfirmView.as_view(template_name='TaskManager/password_reset_confirm.html'),
          name='password_reset_confirm'),
     # ex: password_reset_complete/
     path('password_reset_complete/',
          PasswordResetCompleteView.as_view(template_name='TaskManager/password_reset_complete.html'),
          name='password_reset_complete'),
     # ex: /tm/task_list/
     path('task_list/', views.TaskCreateView.as_view(), name='task_list'),
     # ex: /tm/task_delete/5/
     path('task_delete/<int:pk>', views.task_delete, name='task_delete'),
     # ex: /tm/task_completed/5/
     path('task_completed/<int:pk>', views.task_completed, name='task_completed'),
     # ex: /tm/comment_update/5/
     path('comment_update/<int:pk>', views.UpdateCommentView.as_view(), name='comment_update'),
]
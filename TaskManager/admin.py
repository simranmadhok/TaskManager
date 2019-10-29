from django.contrib import admin
from .models import Task, TaskComments

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','priority','date_created','date_due')
    list_filter = ['priority', 'date_created', 'date_due','completed']
    search_fields = ['title','priority']
    raw_id_fields = ['user']
    ordering = ['-date_due']

class TaskCommentsAdmin(admin.ModelAdmin):
    list_display = ('comments', 'attachment')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComments, TaskCommentsAdmin)

from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import Task

class TaskAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Task
        fields = '__all__'

class TaskAdmin(admin.ModelAdmin):
    form = TaskAdminForm

admin.site.register(Task, TaskAdmin)
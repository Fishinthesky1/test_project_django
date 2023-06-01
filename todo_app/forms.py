from django import forms
from .models import Task
from django.contrib.auth.models import User

status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

class TaskRegistrationForm(forms.ModelForm):
    assign = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    task_name = forms.CharField(max_length=100)
    status = forms.ChoiceField(choices=status)

    class Meta:
        model = Task
        fields = '__all__'

    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.task_name = self.cleaned_data['task_name']
        task.status = self.cleaned_data['status']
        task.save()
        assigns = self.cleaned_data['assign']
        for assign in assigns:
            task.assign.add((assign))

        if commit:
            task.save()

        return task

    def __init__(self, *args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'Name'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['placeholder'] = 'Email'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['assign'].widget.attrs['placeholder'] = 'Found date'

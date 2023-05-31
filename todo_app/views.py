from django.shortcuts import render
from todo_app.forms import TaskRegistrationForm
from todo_app.models import Task

def Tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_in_work = tasks.filter(Status='2')
        complete_tasks = tasks.filter(Status='3')
        context = {
            'tasks' : tasks,
            'complete_tasks' : complete_tasks,
            'tasks_in_work' : tasks_in_work,
        }
    return render(request, 'todo_app/tasklist.html', context)

def newTask(request):
    if request.method == 'POST':
        form = TaskRegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return render(request, 'todo_app/new_task.html', context)
        else:
            return render(request, 'todo_app/new_task.html', context)
    else:
        form = TaskRegistrationForm()
        context = {
            'form': form,
        }
        return render(request,'todo_app/new_task.html', context)

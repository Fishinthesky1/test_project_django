from .models import UserProfile
from .forms import RegistrationForm
from .forms import ProfilePictureForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from todo_app.models import Task

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user = form.save()
            created = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            context = {'created' : created}
            return render(request, 'oauth/reg_form.html', context)
        else:
            return render(request, 'oauth/reg_form.html', context)
    else:
        form = RegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'oauth/reg_form.html', context)


def usersView(request):
    users = UserProfile.objects.all()
    tasks = Task.objects.all()
    context = {
        'users': users,
        'tasks': tasks,
    }
    return render(request, 'oauth/users.html', context)

def user_view(request, profile_id):
    user = UserProfile.objects.get(id=profile_id)
    context = {
        'user_view' : user,
    }
    return render(request, 'oauth/user.html', context)

def profile(request):
    if request.method == 'POST':
        img_form = ProfilePictureForm(request.POST, request.FILES)
        print('PRINT 1: ', img_form)
        context = {'img_form' : img_form }
        if img_form.is_valid():
            img_form.save(request)
            updated = True
            context = {'img_form' : img_form, 'updated' : updated }
            return render(request, 'oauth/profile.html', context)
        else:
            return render(request, 'oauth/profile.html', context)
    else:
        img_form = ProfilePictureForm()
        context = {'img_form' : img_form }
        return render(request, 'oauth/profile.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('user.html')
        else:
            return render(request, 'login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('oauth:login'))

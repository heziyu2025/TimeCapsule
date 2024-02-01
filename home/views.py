from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from datetime import datetime

from .forms import LoginForm
from .models import Capsule
from .forms import SignupForm

def index_view(request):
    # get capsules
    if request.user.is_authenticated:
        user_capsules = Capsule.objects.filter(user=request.user)
    else:
        user_capsules = []

    # get date distence
    current_datetime = datetime.now().date()
    time_to_open = []
    for capsule in user_capsules:
        capsule_date = capsule.open_time
        time_to_open.append((current_datetime - capsule_date).days)

    combined_list = zip(user_capsules, time_to_open)

    # content
    content = {'user': request.user, 
               'combined_list': combined_list}
    
    return render(request, "index.html", content)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    password_wrong = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                password_wrong = True
    else:
        form = LoginForm()

    content = {'form': form,
               'password_wrong': password_wrong}
    
    return render(request, 'login.html', content)

def logout_view(request):
    logout(request)
    return redirect('index')
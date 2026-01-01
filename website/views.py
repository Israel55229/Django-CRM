from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    template_name = 'website/index.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the user information passed into the form to the system
        user = authenticate(request, username= username, password=password)

        # check if there is a logged in user in the system and log them in
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged in!')
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
            return redirect('home')
    context = {}
    return render(request, template_name, context)


def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged out successfully')
    return redirect('home')


def register_user(request):
    template_name = 'website/register.html'
    context = {}
    return render(request, template_name, context)


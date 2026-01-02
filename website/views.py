from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    template_name = 'website/index.html' 
    records = Record.objects.all()

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
    context = {"records": records }
    return render(request, template_name, context)


# View To Create Record
@login_required(login_url='home')
def add_record(request):
    template_name = 'website/add_records.html'
    form = AddRecordForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddRecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successful!")
                return redirect('home')     
        context = {'form': form}
        return render(request, template_name, context) 
    
    else:
        messages.error(request, "Login to add records")
        return redirect('home')




@login_required(login_url='home')
def customer_record(request, pk):
    template_name = 'website/record_detail.html'
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)

        context = {'record': record}
        return render(request, template_name, context)
    else:
        messages.error(request, "You Must Be Logged In To View That Page...")
        return redirect('home')
    

@login_required(login_url='home')
def update_record(request, pk):
    template_name = 'website/add_records.html'
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        form = AddRecordForm(instance=record)
        if request.method == "POST":
            form = AddRecordForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Have Been Updated Successfully...")
                return redirect('home')
            # return messages.error(request, 'An error occured during edition of the record')
        context = {'form': form}
        return render(request, template_name, context)
    
    else:
        messages.error(request, 'You Must Be Logged in To Edit This Record')
        return redirect('home')
    

@login_required(login_url='home')
def delete_record(request, pk):
    template_name = 'website/record_detail.html'
    if request.user.is_authenticated:
        record = get_object_or_404(Record, id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    
        context = { 'record': record }
        return render(request, template_name, context)
    else:
        messages.error(request, "You Must Be Logged In To Do That...")
        return redirect('home')
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged out successfully')
    return redirect('home')


def register_user(request):
    template_name = 'website/register.html'
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            # authenticate the user
            user = authenticate(request, username= username, password= password)

            # Now let log the user in
            if user is not None:
                login(request, user)
                messages.success(request, "You have been regiested and logged in successfully")
                return redirect('home')
            
    context = {'form': form}
    return render(request, template_name, context)


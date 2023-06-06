from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')

        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

from django.contrib.auth.models import User 

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            # form = UserCreationForm(request.POST)
            # if form.is_valid():
                # form.save()
                # return redirect('/')
            user = User.objects.create_user(
                first_name= first_name, 
                last_name= last_name, 
                username= username,
                email = email, 
                password= password )
        
            return redirect('/') 
        
        
        return render(request,'account/login.html')
    else:
        return redirect('/')
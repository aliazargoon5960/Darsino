from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from . forms import RegisterForm, LoginForm
from account_module.models import User
from django.contrib import messages


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home_module:home")
        form = RegisterForm()
        return render(request, "account_module/register.html", {'form': form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # ایمیل به عنوان username
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("home_module:home")
        return render(request, "account_module/register.html", {'form': form})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home_module:home")
        form = LoginForm()
        return render(request, "account_module/login.html", {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('home_module:home')
        return render(request, "account_module/login.html", {'form': form})



def logout_view(request):
    logout(request)
    return redirect("home_module:home")



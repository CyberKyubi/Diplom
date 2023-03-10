from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from . import forms


def register_request(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("homepage")
        messages.error(request, "Неверная информация.")
    form = forms.RegistrationForm()
    return render(request=request, template_name="cabinet/registration/registration.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = forms.LoginAuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("homepage")
            else:
                messages.error(request, "Неверный логин или пароль.")
        else:
            messages.error(request, "Неверный логин или пароль.")
    form = forms.LoginAuthForm()
    return render(request=request, template_name="cabinet/registration/login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    return redirect("homepage")


def cabinet(request):
    return render(request, template_name="cabinet/private/cabinet.html")

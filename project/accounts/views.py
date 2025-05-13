from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

#signup
def user_register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request,"index.html", {"the_register_form": form})


#login
def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = CustomAuthenticationForm()
    return render(request, "registration/login.html", {"the_login_form": form})

def user_logout (request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
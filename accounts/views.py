from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        # User has info and wants an account now
        if request.POST["password0"] == request.POST["password1"]:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(
                    request,
                    "accounts/signup.html",
                    {"error": "Username has already been taken!"},
                )
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password0"]
                )
                auth.login(request, user)
                return redirect("home")
        else:
            return render(
                request, "accounts/signup.html", {"error": "Passwords do not match!"}
            )
    else:
        return render(request, "accounts/signup.html")


def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Username or Password is incorrect!"},
            )
    else:
        return render(request, "accounts/login.html")


def logout(request):
    # Need to be routed to login/home page and to actually log out!
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")


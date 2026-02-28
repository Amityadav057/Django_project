from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from user.forms import LoginForm, RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.set_password(request.POST["password"])
            data.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "user/register.html", context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"],
            )
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('/home')

    context = {"form": form}
    return render(request, "user/login.html", context)


def logout_user(request):
    logout(request)
    return redirect('/user/login')
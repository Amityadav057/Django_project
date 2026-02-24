from django.shortcuts import redirect, render

from user.forms import RegisterForm

# Create your views here.


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form":form
    }
    return render(request, 'user/register.html', context)
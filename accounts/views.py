from django.shortcuts import render, redirect
from django.contrib.auth import (

    authenticate,
    get_user_model,
    login,
    logout,
)

from django.views.decorators.csrf import csrf_protect

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.

@csrf_protect
def login_view(request, *args, **kwargs):

    next = request.GET.get("next")
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user=user)
        if next:
            return redirect(next)


        # redirect
        return redirect("blogs:blogs_index")

    title = "LOGIN"
    context = {
        "form": form,
        "title": title
    }

    return render(request, "accounts/form.html", context)

@csrf_protect
def register_view(request):
    title = "Register"
    next = request.GET.get("next")
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, user=new_user)
        if next:
            return redirect(next)
        # redirect
        return redirect("blogs:blogs_index")

    context = {
        "title": title,
        "form": form
    }

    return render(request, "accounts/form.html", context)


def logout_view(request):
    logout(request)
    #redirect
    return redirect("blogs:blogs_index")

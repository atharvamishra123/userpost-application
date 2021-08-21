import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from user.forms import UserCreationForm, PostForm
from django.http import HttpResponseRedirect


# Create your views here.

def user_registration(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = UserCreationForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    print("user_login called")
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)

        if fm.is_valid():
            uname = fm.cleaned_data['username']
            print(uname)
            upass = fm.cleaned_data['password']
            print(upass)
            user = authenticate(username=uname, password=upass)
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/add/')
    else:
        fm = AuthenticationForm()
    return render(request, "userlogin.html", {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


def add_post(request):
    print("addpost runn")
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_obj = post_form.save(commit=False)
            post_obj.user = request.user
            post_obj.save()
    else:
        post_form = PostForm()
    return render(request, "addpost.html", {"form": post_form})

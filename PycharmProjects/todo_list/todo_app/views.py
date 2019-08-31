from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, UserRegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.save()
            all_items = List.objects.filter(user_id=request.user)
            messages.success(request, 'Item just has been added! ;)', extra_tags='items')
            return render(request, 'home.html', {'all_items': all_items})

    else:
        all_items = List.objects.filter(user_id=request.user)
        return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'Item has been deleted! ;(', extra_tags='items')
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Your account just has been created! you are now able to log in ....', extra_tags='register')
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been just logged out!', extra_tags='logout')
    return redirect('login')


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ' Your password is successfully changed ....', extra_tags='password')
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form': form})



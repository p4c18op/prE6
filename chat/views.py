from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm, UserUpdateForm, AccUpdateForm
from .import models

def index(request):
    users = User.objects.all().exclude(pk=request.user.id)
    rooms = models.Room.objects.all()
    return render(request, 'html/index.html')

def room(request, room_name):
    return render(request, 'html/room.html', {
        'room_name': room_name
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'html/registration/signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        acc_update_form = AccUpdateForm(request.POST, request.FILES, instance=request.user.account)
        if user_update_form.is_valid() and acc_update_form.is_valid():
            user_update_form.save()
            acc_update_form.save()
            messages.success(request, 'Профиль обновлен.')
            return redirect('account')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        acc_update_form = AccUpdateForm(instance=request.user.account)
    
    context = {
        'user_update_form': user_update_form,
        'account_update_form': acc_update_form
    }
    return render(request, 'account.html', context)

from django.shortcuts import render
from .models import User
from .apps import UsersConfig


app_name = UsersConfig.name


def user(request):
    return render(request, f'{app_name}/user.html')

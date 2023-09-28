from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User
from .apps import UsersConfig
from .serializers import UserSerializer

app_name = UsersConfig.name

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user(request):
    return render(request, f'{app_name}/user.html')

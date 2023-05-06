from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Customuser, Customuserprofile
from .serializer import CustomuserSerializer, UserprofileSerializer

# Create your views here.
class Customuserview(ModelViewSet):
    serializer_class = CustomuserSerializer
    queryset = Customuser.objects.all()

class Profileview(ModelViewSet):
    serializer_class = UserprofileSerializer
    queryset = Customuser.objects.all()
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Customuser, Customuserprofile, Address_global
from .serializer import CustomuserSerializer, UserprofileSerializer
from django_seed import Seed


seeder = Seed.seeder()
seeder.add_entity(Customuserprofile, 4)

def execute():
    seeder.execute()
    print("seeded successfully")
# Create your views here.
class Customuserview(ModelViewSet):
    serializer_class = CustomuserSerializer
    queryset = Customuser.objects.all()

class Profileview(ModelViewSet):
    serializer_class = UserprofileSerializer
    queryset = Customuserprofile.objects.select_related("user", "address")
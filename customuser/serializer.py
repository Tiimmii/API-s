from rest_framework import serializers
from .models import Customuserprofile, Customuser, Address_global

class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ("email", "name", "created_at", "updated_at")

class AddressSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Address_global
        fields = '__all__'

class UserprofileSerializer(serializers.ModelSerializer):
    user = CustomuserSerializer()
    address = AddressSerailizer()
    class Meta:
        model = Customuserprofile
        fields = "__all__"
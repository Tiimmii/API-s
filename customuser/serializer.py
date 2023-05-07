from rest_framework import serializers
from .models import Customuserprofile, Customuser, Address_global

class AddressSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Address_global
        fields = '__all__'

class UserprofileSerializer(serializers.ModelSerializer):
    address = AddressSerailizer()
    class Meta:
        model = Customuserprofile
        fields = "__all__"

class CustomuserSerializer(serializers.ModelSerializer):
    user_profile = UserprofileSerializer()
    class Meta:
        model = Customuser
        fields = ("email", "name", "created_at", "updated_at", "user_profile")


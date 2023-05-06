from rest_framework import serializers
from .models import Customuserprofile, Customuser

class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ("email", "name", "created_at", "updated_at")

class UserprofileSerializer(serializers.ModelSerializer):
    user = CustomuserSerializer()
    class Meta:
        model = Customuserprofile
        fields = "__all__"
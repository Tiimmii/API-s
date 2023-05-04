import jwt
from django.shortcuts import render
from .models import Jwt
from customuser.models import Customuser
from datetime import datetime, timedelta
from django.conf import settings
import random, string
from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, RefreshSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response

# Create your views here.
def get_random(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_access_token(payload):
    return jwt.encode(
        {"exp": datetime.now() + timedelta(minutes=5), **payload},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

def get_refresh_token():
    return jwt.encode(
        {"exp": datetime.now() + timedelta(days=365), "data": get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
    )

class Loginview(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(username=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if not user:
            return Response({"error": "Invalid email or password"}, status="400")

        Jwt.objects.filter(user_id=user.id).delete()

        access = get_access_token({"user":user.id})
        refresh = get_refresh_token()

        Jwt.objects.create(user_id = user.id, access_token = access, refresh_token= refresh)
        #decode() removes the b' which may prevent validation    
        return Response({"access_token":access, "refresh_token": refresh})
        #here the JSON decodes automatically
class Registerview(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        Customuser.objects.create_user(**serializer.validated_data)

        return Response({"success": "user created."}, status=200)
    
def valid_token(token):
    try:
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
    except Exception:
        return None
    
    exp = decoded_data["exp"]

    if datetime.now().timestamp() > exp:
        return None
    
    return decoded_data
class Refreshview(APIView):
    serializer_class = RefreshSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            active_jwt=Jwt.objects.get(refresh_token=serializer.validated_data["refresh_token"])
        except Jwt.DoesNotExist:
            return Response({"error": "refresh token not found"}, status="400")
        
        if not valid_token(active_jwt.refresh_token):
            return Response({"error": "token not valid or expired"}, status="400")
        
        access_token = get_access_token({"user_id":active_jwt.user.id})
        refresh_token = get_refresh_token()

        active_jwt.access_token = access_token
        active_jwt.refresh_token = refresh_token
        active_jwt.save()

        return Response({"access_token":access_token, "refresh_token": refresh_token}, status="200")

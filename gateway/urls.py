from django.urls import path
from .views import Loginview, Registerview

urlpatterns = [
    path('login/', Loginview.as_view()),
    path('register/', Registerview.as_view()),
]
from django.urls import path
from .views import Loginview, Registerview, Refreshview

urlpatterns = [
    path('login/', Loginview.as_view()),
    path('register/', Registerview.as_view()),
    path('refresh/', Refreshview.as_view())
]
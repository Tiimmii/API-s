from django.urls import path, include
from .views import people, detail, postoperation

urlpatterns = [
    path('people/', people),
    path('detail/<int:pk>/', detail),
    path('opr/', postoperation),
]
from django.urls import path, include
from rest_framework import routers
from.views import Eventview

router = routers.DefaultRouter()
router.register('event-main', Eventview)

urlpatterns = [
    path('', include(router.urls))
]
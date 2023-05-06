from django.urls import path, include
from .views import Customuserview, Profileview
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userview', Customuserview)
router.register('profileview', Profileview)

urlpatterns = [
    path('', include(router.urls))
]

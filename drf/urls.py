from django.urls import path, include
from .views import people, detail, peopleAPIView, detailAPIView, genericAPIView, peopleViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register('peopleViewset', peopleViewset, basename='people')

urlpatterns = [
    path('people/', people),
    path('detail/<int:pk>/', detail),
#    path('opr/', postoperation),
    path('peopleAPIView/', peopleAPIView.as_view()),
    path('detailAPIView/<int:pk>/', detailAPIView.as_view()),
    path('genericAPIview/<int:id>/', genericAPIView.as_view()),
    path('', include(router.urls)),
]

# urlpatterns += router.urls
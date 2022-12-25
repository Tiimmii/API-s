from django.urls import path, include
from .views import people, detail, peopleAPIView, detailAPIView

urlpatterns = [
    path('people/', people),
    path('detail/<int:pk>/', detail),
#    path('opr/', postoperation),
    path('peopleAPIView/', peopleAPIView.as_view()),
    path('detailAPIView/<int:pk>/', detailAPIView.as_view()),
]
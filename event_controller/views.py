from django.shortcuts import render
from .models import EventMain, EventAttender, EventFeature
from .serializer import EventmainSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class Eventview(ModelViewSet):
    serializer_class = EventMain
    queryset = EventMain.objects.select_related("user_event_author", "event_address")

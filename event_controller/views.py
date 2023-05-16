from django.shortcuts import render
from .models import EventMain, EventAttender, EventFeature
from .serializer import EventmainSerializer, EventFeatureSerializer
from rest_framework.viewsets import ModelViewSet
from customuser.serializer import AddressSerailizer
# Create your views here.
class Eventview(ModelViewSet):
    serializer_class = EventmainSerializer
    queryset = EventMain.objects.select_related("author", "address_info").prefetch_related("event_feature")

    def create(self, request, *args, **kwargs):
        a_serializer = AddressSerailizer(data=request.data)
        a_serializer.is_valid(raise_exception=True)
        a_serializer.save()

        data = {**request.data, "address_info_id":a_serializer["id"]}

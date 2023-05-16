from django.shortcuts import render
from .models import EventMain, EventAttender, EventFeature
from .serializer import EventmainSerializer, EventFeatureSerializer
from rest_framework.viewsets import ModelViewSet
from customuser.serializer import AddressSerailizer
from customuser.models import Address_global
# Create your views here.
class Eventview(ModelViewSet):
    serializer_class = EventmainSerializer
    queryset = EventMain.objects.select_related("author", "address_info").prefetch_related("event_feature")

    def create(self, request, *args, **kwargs):
        a_serializer = AddressSerailizer(data=request.data)
        a_serializer.is_valid(raise_exception=True)
        a_serializer.save()

        data = {**request.data, "address_info_id":a_serializer["id"]}
        e_serializer = self.serializer_class(data=data)
        if not e_serializer.is_valid():
            Address_global.objects.filter(id=e_serializer["address_info_id"]).delete()
            raise Exception(e_serializer.errors)
        e_serializer.save()

        features = request.data.get("features", None)
        if not isinstance(list, features):
            features = [features]
        
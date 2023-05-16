from rest_framework import serializers
from customuser.serializer import CustomuserSerializer, AddressSerailizer
from .models import EventMain, EventFeature, EventAttender

class EventFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFeature
        fields = '__all__'

class EventmainSerializer(serializers.ModelSerializer):
    author = CustomuserSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only = True)
    address_info = AddressSerailizer(read_only = True)
    address_info_id = serializers.IntegerField(write_only = True)
    event_feature = EventFeatureSerializer(read_only=True, many=True)

    class Meta:
        model = EventMain
        fields = '__all__'
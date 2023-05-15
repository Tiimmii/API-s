from django.db import models
from customuser.models import Customuser, Address_global
# Create your models here.
class EventMain(models.Model):
    author = models.ForeignKey(Customuser, related_name='user_event_author', on_delete=models.CASCADE)
    address_info = models.ForeignKey(Address_global, related_name='event_address', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    date = models.DateField()
    max_seat = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class EventFeature(models.Model):
    event = models.ForeignKey(EventMain, related_name='event_feature', on_delete=models.CASCADE)
    feature_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name
    
class EventAttender(models.Model):
    event_main = models.ForeignKey(EventMain, related_name='event_attenders', on_delete=models.CASCADE)
    user = models.ForeignKey(Customuser, related_name='user_attendant', on_delete=models.CASCADE)
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
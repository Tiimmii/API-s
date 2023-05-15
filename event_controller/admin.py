from django.contrib import admin
from.models import EventAttender, EventFeature, EventMain
# Register your models here.
admin.site.register((EventAttender, EventFeature, EventMain))

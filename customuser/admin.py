from django.contrib import admin
from .models import Customuser, Customuserprofile, Address_global

admin.site.register(Customuser)
admin.site.register(Customuserprofile)
admin.site.register(Address_global)
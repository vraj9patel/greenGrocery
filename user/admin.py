from django.contrib import admin
from .models import UserProfileInfo, GuestEmail

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(GuestEmail)

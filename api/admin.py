from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Report, UserProfile

# Register your models here.

admin.site.register((
    Report,
    UserProfile,)
)

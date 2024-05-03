from django.contrib import admin

# Register your models here.
from .models import Theatre, Place

# Register your models here.
admin.site.register(Theatre)
admin.site.register(Place)
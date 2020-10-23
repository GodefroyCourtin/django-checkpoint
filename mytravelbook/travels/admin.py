from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Voyage)
admin.site.register(Voyagestep)
admin.site.register(Linkstep) 
from django.contrib import admin

# Register your models here.
from app.models import *

# Register your models here.
admin.site.register(Figures)
admin.site.register(Emotions)
admin.site.register(Locations)
admin.site.register(Events)
from django.contrib import admin
from .models import Mountain, Images, Coordinates, Level, User

admin.site.register(User)
admin.site.register(Mountain)
admin.site.register(Images)
admin.site.register(Coordinates)
admin.site.register(Level)


from django.contrib import admin
from app.models import Location, Category, Image
# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)

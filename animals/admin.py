from django.contrib import admin

# Register your models here.

from animals.models import AnimalCategory, Animal

admin.site.register(AnimalCategory)
admin.site.register(Animal)

from django.contrib import admin

from .models import PetOwner, Pet, Vaccine
# Register your models here.

admin.site.register(Pet)
admin.site.register(PetOwner)
admin.site.register(Vaccine)
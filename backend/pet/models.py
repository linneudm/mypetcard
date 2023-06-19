from django.db import models
from datetime import datetime
# Create your models here.

def vaccine_directory_path(instance, filename):
    return 'vaccine/{0}/{1}'.format(instance.name, filename)

class Gender(models.TextChoices):
    MALE = "M"
    FEMALE = "F"


class PetOwner(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Pet(models.Model):
    GENDER_OPTIONS = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    name = models.CharField(max_length=155, null=False, blank=False)
    gender = models.CharField(max_length=1, null=False, blank=False, choices=Gender.choices, default="M")
    birthday = models.DateField(null=False, blank=False)
    breed = models.CharField(max_length=155, null=True, blank=True)
    owner = models.OneToOneField(PetOwner, on_delete=models.DO_NOTHING, blank=False, null=False)

    @property
    def fullgender(self):
        return "Male" if(self.gender == "M") else "Female"

    def __str__(self):
        return self.name + " / " + self.fullgender +  " / " + self.breed
    
class Vaccine(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    doctor_name = models.CharField(max_length=155, null=False, blank=False)
    crmv = models.CharField(max_length=155, null=True, blank=True)
    picture = models.ImageField(upload_to=vaccine_directory_path, blank=True, null=True)

    def __str__(self):
        return self.name + " / " + datetime.strftime(self.date,"%d/%m/%Y") + " / " + self.doctor_name
class Deworkming(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)
    date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name

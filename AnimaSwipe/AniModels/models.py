from django.db import models
from multiselectfield import MultiSelectField

GENDER = ((1, 'MALE'), 
                (2, 'FEMALE'))
PET_TYPES = ((1, 'DOG'), 
                (2, 'CAT'),
                (3, 'BIRD'))

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    user_age = models.IntegerField(default=0)
    user_password = models.CharField(max_length=20)
    user_gender = MultiSelectField(choices=GENDER)
    user_pitch = models.CharField(max_length=300)
    def user_name(self):
        return first_name + last_name
    def __str__(self):
        return self.first_name
    
class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    pet_type = MultiSelectField(choices=PET_TYPES)
    pet_breed = models.CharField(max_length=20)
    pet_age = models.IntegerField(default=0)
    pet_gender = MultiSelectField(choices=GENDER)
    pet_description = models.CharField(max_length=150)
    def pet_return_name(self):
        return pet_name
    def __str__(self):
        return self.pet_name
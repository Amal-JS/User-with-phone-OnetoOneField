from django.db import models

from django.contrib.auth.models import User
# Create your models here.
from django.core.exceptions import ValidationError



class Phone(models.Model):

    #validator function for checking if length of phone field is equal to 10
    #if not raise error

    def phone_len_checker(value):
        if len(value) <10 or len(value) >10:
            raise ValidationError("10 digit number required")
        

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(unique=True,blank=False,null=False,validators=[phone_len_checker],max_length=10)

    def __str__(self):
        return f"{self.user} : {self.phone}"
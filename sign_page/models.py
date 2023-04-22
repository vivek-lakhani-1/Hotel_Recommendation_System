from pyexpat import model
from django.db import models

class User_sign(models.Model):
    user_name = models.CharField(max_length=100,default='',null=False)
    password = models.CharField(max_length=32,default='',null=False)
    image = models.ImageField(upload_to='images')
    
    phone_number = models.CharField(max_length=10)
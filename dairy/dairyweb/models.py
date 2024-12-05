from django.db import models
from django.utils.timezone import datetime




class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    discription = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)




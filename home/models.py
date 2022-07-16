from django.db import models

# Create your models here.
class Record(models.Model):
    ename=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

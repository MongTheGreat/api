from django.db import models

# Create your models here.

class Form(models.Model):
    first_name = models.CharField(max_length= 32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    mobile_number = models.IntegerField()


class User(models.Model):
    first_name = models.CharField(max_length= 32)
    email = models.CharField(max_length=32)

class Class(models.Model):
    name = models.CharField(max_length= 32)
    subject = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    teacher= models.ForeignKey(User, on_delete=models.CASCADE)


class Learner(models.Model):
    name = models.CharField(max_length=32)

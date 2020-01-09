from django.db import models

# Create your models here.

class App(models.Model):
	soft_name = models.CharField(max_length = 200)
	developer = models.CharField(max_length = 200)
	version = models.IntegerField()
	date = models.DateTimeField("uploaded date")


class User(models.Model):
	user_fname = models.CharField(max_length = 100)
	user_lname = models.CharField(max_length = 100)
	user_email = models.EmailField()

class Device(models.Model):
	device_name = models.CharField(max_length = 100)
	device_model = models.CharField(max_length = 100)


from django.db import models

# Create your models here.
class Person_data(models.Model):
    person_name = models.TextField()
    person_age = models.IntegerField()
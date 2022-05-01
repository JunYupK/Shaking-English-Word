
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class EnglishWord(models.Model):
    english_meaning = models.CharField(max_length=20)
    english_word =  models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    passward = models.CharField(max_length=20)

    def __str__(self):
        return self.name

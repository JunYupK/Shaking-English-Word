
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class EnglishWord(models.Model):
    english_meaning = models.CharField(max_length=20)
    english_word =  models.CharField(max_length=20)
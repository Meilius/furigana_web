from django.db import models
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    label = 'myapp'

default_app_config = 'myapp.MyAppConfig'

class Person(models.Model):
    name = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=20)


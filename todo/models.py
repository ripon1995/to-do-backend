from django.db import models


# Create your models here.

class ToDo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='New task')

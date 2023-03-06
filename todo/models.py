from django.db import models


# Create your models here.

class StatusChoice(models.TextChoices):
    choiceNew = ('NEW', 'New Task')
    choiceRun = ('RUNNING', 'Running Task')
    choiceFuture = ('FUTURE', 'Future Task')


class ToDo(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default=StatusChoice.choiceNew, choices=StatusChoice.choices)

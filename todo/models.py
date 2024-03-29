from django.db import models
from django.utils import timezone
from user.models import User

STATUS_CHOICES = (
    ('New', 'New'),
    ('Active', 'Active'),
    ('Completed', 'Completed'),
    ('Blocked', 'Blocked')
)


# Create your models here.
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    createdDate = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

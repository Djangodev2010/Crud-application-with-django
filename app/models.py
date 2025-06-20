from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    status = models.BooleanField
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

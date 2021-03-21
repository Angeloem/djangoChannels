from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Chat(models.Model):
    message = models.TextField(null=False, blank=False)

    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)

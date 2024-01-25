from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Capsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=1024)
    creat_time = models.DateTimeField(auto_now_add=True)
    open_time = models.DateField()
    is_private = models.BooleanField(default=True)

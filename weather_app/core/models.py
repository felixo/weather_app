from django.contrib.auth.models import User
from django.db import models


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    request = models.CharField(max_length=255)
    response = models.CharField(max_length=255)

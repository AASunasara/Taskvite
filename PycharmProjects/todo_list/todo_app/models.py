from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.pk)


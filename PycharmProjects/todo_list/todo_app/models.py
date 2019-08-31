from django.db import models
from django.contrib.auth.models import User
from datetime import date


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.pk)


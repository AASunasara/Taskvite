from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    objects = models.Manager()


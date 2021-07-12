from django.db import models


class Apps(models.Model):
    name = models.CharField(max_length=100)

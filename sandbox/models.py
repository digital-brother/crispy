from django.db import models


class Server(models.Model):
    domain = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    ip = models.CharField(max_length=16)

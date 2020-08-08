from django.db import models


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issued_by = models.CharField(max_length=50)
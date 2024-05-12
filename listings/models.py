from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)


class Title(models.Model):
    annonce = models.fields.CharField(max_length=150)

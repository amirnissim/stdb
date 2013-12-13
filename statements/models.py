from django.db import models

class Statement(models.Model):
    quote = models.TextField()
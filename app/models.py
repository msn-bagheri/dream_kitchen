from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    description = models.TextField()

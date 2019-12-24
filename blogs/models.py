from django.db import models
from datetime import datetime


# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=30)
    content = models.TextField()
    time = models.DateTimeField(default=datetime.now(), blank=True)
    author = models.CharField(max_length=30, default="admin")


    def __str__(self):
        return self.title


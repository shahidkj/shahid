from django.db import models

# Create your models here.
class task(models.Model):
    name=models.TextField(max_length=250)
    priority=models.IntegerField()
    def __str__(self):
        return self.name
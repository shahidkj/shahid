from django.db import models

# Create your models here.
class second(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='images')
    desc=models.TextField()
    def __str__(self):
        return self.name
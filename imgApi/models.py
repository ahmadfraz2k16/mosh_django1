from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    size = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100)

    def __str__(self):
        return self.name

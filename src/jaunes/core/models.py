from django.db import models
from taggit.managers import TaggableManager


class Business(models.Model):
    city = models.CharField(max_length=255)
    quarter = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='business')
    tags = TaggableManager()

    def __str__(self):
        return self.name

from django.db import models
from slugify import slugify

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name 

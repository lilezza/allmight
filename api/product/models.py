from django.db import models
from producttag.models import Brand , Tag , Categories
from slugify import slugify

class Product(models.Model):
    brand = models.ForeignKey (Brand , on_delete = models.CASCADE , related_name = 'products')
    category = models.ForeignKey (Categories , on_delete = models.CASCADE ,related_name = 'products')
    tag = models.ForeignKey (Tag , on_delete = models.CASCADE , related_name = 'products')

    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    slug = models.SlugField(unique = True )

    primary_image = models.ImageField(upload_to = 'products/')
    price = models.DecimalField(max_digits = 12 , decimal_places=0)
    quantity = models.PositiveIntegerField()
    delivery_amount = models.DecimalField(max_digits = 12 , decimal_places=0)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args , **kwargs)
    
    def __str__(self):
        return self.name

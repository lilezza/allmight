from rest_framework import serializers
from .models import Product , ProductImage
from producttag.models import Brand , Tag , Categories
from slugify import slugify

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id' , 'brand' , 'category' , 'tag' , 'name' , 'description' , 'slug' , 'primary_image' , 'price' , 'quantity' , 'delivery_amount']


    def validate_slug(self, value):
        if not value.isascii():
            raise serializers.ValidationError("Slug باید فقط از حروف انگلیسی، اعداد و خط تیره تشکیل شده باشد.")
        
        # بررسی یکتا بودن slug
        queryset = Product.objects.filter(slug=value)
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError("Slug باید یکتا باشد.")
        
        return value

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id' , 'product' , 'image']
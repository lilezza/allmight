from rest_framework import serializers
from .models import Tag
from slugify import slugify
import re

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id' , 'name' , 'slug']

    def validate_slug(self, value):
        if not re.match(r'^[a-zA-Z0-9-]+$', value):
            raise serializers.ValidationError("slug فقط باید شامل حروف انگلیسی، عدد و خط تیره باشه.")
        
        qs = Tag.objects.filter(slug=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("این slug قبلاً استفاده شده.")


        return value

    def validate(self, data):
        # اگر اسلاگ داده نشده بود، بساز از روی name
        if not data.get('slug') and data.get('name'):
            data['slug'] = slugify(data['name'])

        return data

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # هنگام آپدیت هم اگر slug داده نشده بود، بساز
        if not validated_data.get('slug') and validated_data.get('name'):
            validated_data['slug'] = slugify(validated_data['name'])
        return super().update(instance, validated_data)
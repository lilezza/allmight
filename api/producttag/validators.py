import re
from rest_framework import serializers
from slugify import slugify

def validate_slug_format(value):
    if not re.match(r'^[a-zA-Z0-9-]+$', value):
        raise serializers.ValidationError("slug فقط باید شامل حروف انگلیسی، عدد و خط تیره باشه.")
    return value

def validate_unique_slug_for_model(model_class, value, instance=None):
    qs = model_class.objects.filter(slug=value)
    if instance:
        qs = qs.exclude(pk=instance.pk)
    if qs.exists():
        raise serializers.ValidationError("این slug قبلاً استفاده شده.")
    return value

def auto_generate_slug(data):
    if not data.get('slug') and data.get('name'):
        data['slug'] = slugify(data['name'])
    return data

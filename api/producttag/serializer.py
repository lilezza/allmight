from rest_framework import serializers
from .models import Tag , Brand , Categories , Attribute
from .validators import validate_slug_format , validate_unique_slug_for_model , auto_generate_slug

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id' , 'name' , 'slug']

    def validate_slug(self, value):
        value = validate_slug_format(value)
        return validate_unique_slug_for_model(Tag, value, self.instance)

    def validate(self, data):
        return auto_generate_slug(data)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = auto_generate_slug(validated_data)
        return super().update(instance, validated_data)
    

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id' , 'name' , 'slug']

    def validate_slug(self, value):
        value = validate_slug_format(value)
        return validate_unique_slug_for_model(Brand, value, self.instance)

    def validate(self, data):
        return auto_generate_slug(data)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = auto_generate_slug(validated_data)
        return super().update(instance, validated_data)
    
class CategoryParentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = ['id' , 'name' , 'slug']

class CategoriesSerializer(serializers.ModelSerializer):
    parent = CategoryParentSerializer(read_only=True)
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset=Categories.objects.all(), source='parent', write_only=True, required=False
    )

    class Meta:
        model = Categories
        fields = ['id' , 'name' , 'slug' , 'parent' , 'parent_id']

    def validate_slug(self, value):
        value = validate_slug_format(value)
        return validate_unique_slug_for_model(Categories, value, self.instance)

    def validate(self, data):
        return auto_generate_slug(data)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data = auto_generate_slug(validated_data)
        return super().update(instance, validated_data)
    

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id' , 'name']
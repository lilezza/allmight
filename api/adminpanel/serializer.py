from rest_framework import serializers
from .models import CustomUser

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    is_staff = serializers.BooleanField(default=False)  # اضافه کردن فیلد نقش
    is_superuser = serializers.BooleanField(default=False)  # اضافه کردن فیلد نقش

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        # دریافت مقادیر is_staff و is_superuser از ورودی
        is_staff = validated_data.pop('is_staff', False)
        is_superuser = validated_data.pop('is_superuser', False)

        # ایجاد کاربر
        user = CustomUser(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            phone_number=validated_data.get('phone_number', '')
        )
        user.set_password(validated_data['password'])

        # تنظیم نقش‌ها
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user

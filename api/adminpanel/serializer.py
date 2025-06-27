from rest_framework import serializers
from .models import CustomUser , UserAddress

class AdminUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True , required = True)
    is_staff = serializers.BooleanField(default=False)  # اضافه کردن فیلد نقش
    is_superuser = serializers.BooleanField(default=False)  # اضافه کردن فیلد نقش

    class Meta:
        model = CustomUser
        fields = ['id','username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        """ اجباری بودن فیلدها فقط برای ایجاد کاربر بررسی می‌شود """
        super().__init__(*args, **kwargs)
        if self.instance:
            # اگر در حالت update هستیم، همه فیلدها اختیاری باشند
            for field in self.fields:
                self.fields[field].required = False

    def validate(self, data):
        """ بررسی اجباری بودن فیلدها فقط هنگام ساخت کاربر """
        if self.instance is None:  # یعنی در حالت create هستیم
            required_fields = ['username', 'email', 'password']
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                raise serializers.ValidationError({field: "این مقدار لازم است." for field in missing_fields})

        return data

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

        password = validated_data['password']
        user.set_password(password)

        # تنظیم نقش‌ها
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        return user
    
    def update(self , instance , validated_data):
        for attr , value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance , attr , value)
        
        instance.save()
        return instance
    
class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id' , 'user' , 'province' , 'city' , 'title' , 'address' , 'phone_number' , 'home_phone_number']
        

    # def update (self , instance , validated_data):
    #     instance.username = validated_data.get('username' , instance.username)
    #     instance.first_name = validated_data.get('first_name' , instance.first_name)
    #     instance.last_name = validated_data.get('last_name' , instance.last_name)
    #     instance.email = validated_data.get('email' , instance.email)
    #     instance.phone_number = validated_data.get('phone_number' , instance.phone_number)
    #     instance.is_staff = validated_data.get('is_staff' , instance.is_staff)
    #     instance.is_superuser = validated_data.get('is_superuser' , instance.is_superuser)

    #     if 'password' in validated_data:
    #         instance.set_password(validated_data['password'])
        
    #     instance.save()
    #     return instance

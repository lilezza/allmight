from rest_framework import serializers
from .models import CustomUser

class AdminUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model : CustomUser
        fields = ['username' , 'first_name' , 'last_name' , 'emial' , 'phone_number' , 'password']

    def create(self , validate_data):
        user = CustomUser(
            username = validate_data['username'] ,
            first_name = validate_data('first_name' , ''),
            last_name = validate_data('last_name' , ''),
            email = validate_data['email'],
            phone_number = validate_data('phone_number' , '')
        )
        user.set_password(validate_data['password'])

        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

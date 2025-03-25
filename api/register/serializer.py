from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from register.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True , required = True)

    class Meta:
        model = CustomUser
        fields = ['id' , 'username' , 'first_name' , 'last_name' , 'email' , 'phone_number' , 'password']

    def create(self , validate_data):
        user = CustomUser.object.create_user(
            username = validate_data['username'] ,
            email = validate_data['email'],
            first_name = validate_data('first_name' ,''),
            last_name = validate_data('last_name' ,''),
            phone_number = validate_data('phone_number' , ''),
            password = validate_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

    def validate(self , data):
        user = authenticate(email = data['email'] , password = data['password'])
        if user is None:
            raise serializers.ValidationError("ایمیل یا رمز عبور اشتباه است")
        return user
    
    def get_token(self , user):
        refresh = RefreshToken.for_user(user)
        return{
            "refresh" : str(refresh) ,
            "access" : str(refresh.access_token),
        }
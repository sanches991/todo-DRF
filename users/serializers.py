from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        extra_kwargs = {
            "password": {
                'write_only': True
            }
        }

    def create(self,validated_data):
        return CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
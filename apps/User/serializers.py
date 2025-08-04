from rest_framework import serializers
from .models import CustomUser, Location


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'customer_number', 'company_name', 'name', 'email', 'phone', 'address']     
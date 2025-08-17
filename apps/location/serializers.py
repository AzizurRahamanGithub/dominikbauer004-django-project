from rest_framework import serializers
from .models import Location
from apps.User.models import CustomUser



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields= "__all__"

class UserSelectLocationSerializer(serializers.ModelSerializer):
    pucest_locations = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), required=True)

    class Meta:
        model = CustomUser
        fields = ['delivery_locations']
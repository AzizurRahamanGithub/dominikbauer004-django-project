from rest_framework import serializers
from .models import NewsPortal

class NewsPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPortal
        fields = ['id', 'title', 'issue_number', 'issue_date', 'image', 'external_link']

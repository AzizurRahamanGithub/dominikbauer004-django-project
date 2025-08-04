from rest_framework import serializers
from .models import InquiryImage, Inquiry

class InquiryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryImage
        fields = ['id', 'image']

class InquirySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='user.company_name', read_only=True)
    name = serializers.CharField(source='user.name', read_only=True)
    contact_person_name = serializers.CharField(source='contact_person.name', read_only=True)
    contact_person_email = serializers.EmailField(source='contact_person.email', read_only=True)
    contact_person_phone = serializers.CharField(source='contact_person.phone', read_only=True)
    images = InquiryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Inquiry
        fields = [
            'id', 'offer_number', 'created_at', 'company_name', 'name',
            'phone', 'description', 'contact_person_name', 'contact_person_email',
            'contact_person_phone', 'images'
        ]

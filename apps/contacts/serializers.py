

from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User= get_user_model()

class ContactPersonSerializer(serializers.ModelSerializer):
    contact_persons = serializers.SerializerMethodField()

    class Meta:
        model = ContactAssignment
        fields = ['id', 'contact_persons']

    def get_contact_persons(self, obj):
        return [
            {
                "id": person.id,
                "Customer Number": person.customer_number,
                "name": person.name,
                "email": person.email,
                
            }
            for person in obj.contact_persons.all()
        ]

   
        
class UserSelectContactSerializer(serializers.ModelSerializer):
    selected_contact_name = serializers.CharField(source="selected_contact.name", read_only=True)
    selected_contact_email = serializers.EmailField(source="selected_contact.email", read_only=True)
    selected_contact_number = serializers.CharField(source="selected_contact.customer_number", read_only=True)

    class Meta:
        model = UserSelectedContact
        fields = [
            'selected_contact', 
            'selected_contact_number',
            'selected_contact_name',
            'selected_contact_email',
            
        ]



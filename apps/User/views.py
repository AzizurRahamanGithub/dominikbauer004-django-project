from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.contacts.models import ContactAssignment, UserSelectedContact
from apps.Authentication.views import BaseAPIView
from apps.contacts.serializers import ContactPersonSerializer, UserSelectContactSerializer
from apps.location.serializers import LocationSerializer, UserSelectLocationSerializer
from .serializers import UserInfoSerializer
from .models import CustomUser
from apps.location.models import Location

class UserProfileInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        response_data = {}

        # User Details
        user_serializer = UserInfoSerializer(user)
        response_data["user_info"] = user_serializer.data

        # Assigned Contact Persons
        try:
            assignment = ContactAssignment.objects.get(owner=user)
            contact_persons = assignment.contact_persons.all()
            assigned_serializer = ContactPersonSerializer(assignment)
            response_data["assigned_contact_persons"] = assigned_serializer.data
        except ContactAssignment.DoesNotExist:
            response_data["assigned_contact_persons"] = []

        # Selected Contact Person
        selected_contact = UserSelectedContact.objects.filter(owner=user).first()
        if selected_contact:
            selected_serializer = UserSelectContactSerializer(selected_contact)
            response_data["selected_contact_person"] = selected_serializer.data
        else:
            response_data["selected_contact_person"] = None

        # All Locations (assigned by admin)
        all_locations = Location.objects.all()
        location_serializer = LocationSerializer(all_locations, many=True)
        response_data["assigned_locations"] = location_serializer.data

        # Selected Location
        if user.pucest_locations:
            selected_location_serializer = LocationSerializer(user.pucest_locations)
            response_data["selected_location"] = selected_location_serializer.data
        else:
            response_data["selected_location"] = None

        return Response({
            "message": "User profile info fetched successfully",
            "data": response_data
        })
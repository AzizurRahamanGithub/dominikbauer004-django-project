from django.shortcuts import render
from apps.Authentication.views import BaseAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSelectLocationSerializer, LocationSerializer
from .models import Location

# Create your views here.

class UserSelectLocationView(BaseAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.user
        serializer = UserSelectLocationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.success_response( "Location selected successfully.", data= serializer.data)
        return self.error_response( "Not Update", serializer.errors, )
    
class AllLocationView(BaseAPIView):
    permission_classes=[AllowAny]
    
    def get (self, request):
        locations= Location.objects.all()
        serializer= LocationSerializer(locations, many= True)
        
        return self.success_response("Locations Retrive Successfully", data= serializer.data)

from django.urls import path, include
from .views import UserSelectLocationView, AllLocationView


urlpatterns = [
    path('select-location/', UserSelectLocationView.as_view(),   name='user-select-location'),
    path('assigned-locations/', AllLocationView.as_view(), name='all-locations')
]
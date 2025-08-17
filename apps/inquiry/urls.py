from django.urls import path
from .views import InquiryCreateAPIView, OfferListAPIView, OfferDetailAPIView

urlpatterns = [
    path('create/', InquiryCreateAPIView.as_view(), name='inquiry-create'),
    path('offers/', OfferListAPIView.as_view(), name='offer-list'),
    path('offers/<int:pk>/', OfferDetailAPIView.as_view(), name='offer-detail'),

]

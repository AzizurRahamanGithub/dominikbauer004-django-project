from django.urls import path
from .views import NewsPortalListView

urlpatterns = [
    path("list/", NewsPortalListView.as_view(), name="all-news-list")
]

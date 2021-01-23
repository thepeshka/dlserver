from django.urls import path
from .views import get_view_link, get_download_link

urlpatterns = [
    path('dl/<hashid>', get_download_link),
    path('<hashid>', get_view_link),
]

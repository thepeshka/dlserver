from django.urls import path
from .views import get_direct_link

urlpatterns = [
    path('dl/<hashid>', get_direct_link),
]

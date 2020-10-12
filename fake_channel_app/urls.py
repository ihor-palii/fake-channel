from django.urls import path
from .views import simulate_response_on


urlpatterns = [
    path('', simulate_response_on),
]
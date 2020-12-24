from django.urls import path, include
from profile_api.views import HelloApiView


urlpatterns = [
    path('profile/', HelloApiView.as_view())
]
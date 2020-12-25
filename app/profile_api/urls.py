from django.urls import path, include
from profile_api.views import HelloApiView
from profile_api.views import HelloViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='viewset')

urlpatterns = [
    path('profile/', HelloApiView.as_view()),
    path('', include(router.urls))
]
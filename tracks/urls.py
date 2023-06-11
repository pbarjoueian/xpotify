from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tracks.views import TrackViewSet

router = DefaultRouter()
router.register("", TrackViewSet, basename="root")

urlpatterns = [
    path("", include(router.urls)),
]

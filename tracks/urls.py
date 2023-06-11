# config/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tracks.views import TrackView

router = DefaultRouter()
router.register("", TrackView, basename="root")

urlpatterns = [
    path("", include(router.urls)),
]

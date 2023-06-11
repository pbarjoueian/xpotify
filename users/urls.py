from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import UserHistoryView, UserTrackRecommendViewSet

router = DefaultRouter()
router.register("", UserTrackRecommendViewSet, basename="root")

urlpatterns = [
    path(
        "history/",
        UserHistoryView.as_view(),
        name="history",
    ),
    path("recommendation/", include(router.urls), name="recommendation"),
]

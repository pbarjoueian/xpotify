from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from tracks.models import Track
from tracks.serializers import TrackSerializer
from tracks.utils import delete_cache


class TrackViewSet(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    http_method_names = ["get", "post", "patch", "delete"]

    def get_permissions(self):
        """Set custom permissions per each action."""
        if self.action in ["update", "partial_update", "create", "destroy"]:
            self.permission_classes = [
                permissions.IsAdminUser,
            ]
        elif self.action in ["list", "retrieve"]:
            self.permission_classes = [
                permissions.IsAuthenticated,
            ]
        return super().get_permissions()

    CACHE_KEY_PREFIX = "track-view"

    @method_decorator(cache_page(300, key_prefix=CACHE_KEY_PREFIX))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        delete_cache(self.CACHE_KEY_PREFIX)
        return response

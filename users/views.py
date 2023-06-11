from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Count
from rest_framework import permissions, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from tracks.models import Track
from tracks.serializers import TrackSerializer
from users.serializers import UserHistorySerializer

User = get_user_model()


class UserHistoryView(RetrieveUpdateAPIView):
    serializer_class = UserHistorySerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ["patch"]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        history = self.request.user.history
        history.append(request.data["track_id"])
        serializer = self.serializer_class(
            request.user, data={"history": history}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTrackRecommendViewSet(GenericViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ["get"]

    def list(self, request):
        user = request.user
        history = user.history
        clusters = (
            Track.objects.filter(uuid__in=history)
            .values("cluster_number")
            .annotate(the_count=Count("cluster_number"))
        )
        most_favorited_cluster: int = 0
        most_favorited_cluster_count: int = 0
        for cluster in clusters:
            if cluster["the_count"] > most_favorited_cluster_count:
                most_favorited_cluster = cluster["cluster_number"]
                most_favorited_cluster_count = cluster["the_count"]
        queryset = (
            Track.objects.filter(cluster_number=most_favorited_cluster)
            .exclude(uuid__in=history)
            .order_by("?")
            .first()
        )
        serializer = TrackSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

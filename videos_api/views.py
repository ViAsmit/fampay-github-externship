from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework import generics
from videos.models import Video
from .serializers import VideoSerializer


def calling():
    print("yyy")


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

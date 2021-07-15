from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from rest_framework import generics
from videos.models import Video
from .serializers import VideoSerializer


class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class SearchVideoList(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        qs = Video.objects.all()
        query = self.request.query_params.get('q', None)
        print(query)
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs

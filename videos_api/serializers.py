from rest_framework import serializers
from videos.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'description', 'video_url',
                  'thumbnail_url', 'published_date')

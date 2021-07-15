from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_key = models.CharField(max_length=100)
    video_url = models.URLField(null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

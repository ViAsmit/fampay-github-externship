from django.urls import path
from django.views.generic import TemplateView
from .views import VideoList

app_name = "videos_api"

urlpatterns = [
    path('', VideoList.as_view(), name='video-list'),
]
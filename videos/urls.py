from django.urls import path
from django.views.generic import TemplateView

app_name = "videos"

urlpatterns = [
    path('', TemplateView.as_view(template_name='videos/index.html')),
]
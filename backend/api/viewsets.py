from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from .serializers import *
from .models import *

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
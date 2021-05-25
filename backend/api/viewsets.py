from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets,filters,status
from .serializers import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']
    
    @action(detail=False)
    def new(self, request, *args, **kwargs):
        queryset = Video.objects.all().order_by('-timestamp')[:15]
        serializer = VideoSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['title']

    @action(detail=False)
    def new(self, request, *args, **kwargs):
        queryset = Doc.objects.all().order_by('-timestamp')[:15]
        serializer = DocSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CourseViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    search_fields = ['title']

    @action(detail=False)
    def new(self, request, *args, **kwargs):
        queryset = Course.objects.all().order_by('-timestamp')[:15]
        serializer = CourseSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectViewSet(viewsets.ModelViewSet):
    search_fields = ['title','desc']
    filter_backends = (filters.SearchFilter,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    search_fields = ['title']

    @action(detail=False)
    def new(self, request, *args, **kwargs):
        queryset = Project.objects.all().order_by('-timestamp')[:15]
        serializer = ProjectSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagViewSet(viewsets.ModelViewSet):
    search_fields = ['tag_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    ordering_fields = ['-timestamp']
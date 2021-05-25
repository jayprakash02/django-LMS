from rest_framework import serializers
from .models import *

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('url', 'title', 'desc', 'image', 'timestamp','video')

class DocSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doc
        fields = ('url', 'title', 'desc', 'timestamp')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'title', 'desc', 'image', 'timestamp','video','doc')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'title', 'desc', 'image', 'timestamp','video','doc')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
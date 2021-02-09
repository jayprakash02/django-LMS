from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'title', 'desc', 'image', 'timestamp')
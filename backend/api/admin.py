from django.contrib import admin
from .models import Course,Video,Comment
# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Comment)
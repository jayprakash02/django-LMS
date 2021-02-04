from django.contrib import admin
from .models import Course,Video,Comment,Author
# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Author)
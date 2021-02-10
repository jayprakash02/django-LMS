from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Author)

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    class Media:
        js= ('admin/doc.js',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Media:
        js= ('admin/doc.js',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class Media:
        js= ('admin/doc.js',)

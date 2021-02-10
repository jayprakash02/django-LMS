from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Author)

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
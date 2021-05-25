from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# @admin.register(Course,Project,Video,Doc)
# class SummernoteAdmin(SummernoteModelAdmin):
#     summernote_fields = ('desc',)

@admin.register(Course,Project,Video,Doc)
class ImportExportAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Tag)
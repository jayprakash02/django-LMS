from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.
class SummernoteAdmin(SummernoteModelAdmin):
    summernote_fields = ('desc',)

admin.site.register(Video,SummernoteAdmin)
admin.site.register(Doc,SummernoteAdmin)
admin.site.register(Course,SummernoteAdmin)
admin.site.register(Project,SummernoteAdmin)
admin.site.register(Comment)
admin.site.register(Author)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from .api.viewsets import *

router = routers.DefaultRouter()
router.register('doc', DocViewSet)
router.register('course', CourseViewSet)
router.register('video', VideoViewSet)
router.register('project', ProjectViewSet)
router.register('tag', TagViewSet)


urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),

    #Django-allauth
    path('accounts/', include('allauth.urls')),

    #Django-rest-auth
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    #SummoerNote
    path('summernote/', include('django_summernote.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

from .api.views import index_view

router = routers.DefaultRouter()
#router.register('messages', MessageViewSet)

urlpatterns = [
    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

    #Django-allauth
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



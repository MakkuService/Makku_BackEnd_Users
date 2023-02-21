"""Makku_BackEnd URL Configuration

"""

from django.contrib import admin
from django.urls import path, include
#from users.views import index
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="REST_API_Users",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.g/",
      contact=openapi.Contact(email="contact@l"),
      license=openapi.License(name="Open License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
#    path("admin/", admin.site.urls),
#    path("", index, name="home"),
#    path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("users/", include('users.urls')),
]

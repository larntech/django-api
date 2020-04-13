"""larntech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from rest_framework import permissions,routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

from tutorials import views
from tutorials.views import CustomObtainAuthToken

schema_view = get_schema_view(
   openapi.Info(
      title="Tutorials API",
      default_version='v1',
      description="API Description",
      contact=openapi.Contact(email="richard@larntech.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


routers = routers.DefaultRouter()
routers.register(r'api/users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   # url(r'^authenticate/', CustomObtainAuthToken.as_view()),
   url('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api/', include(routers.urls)),

]

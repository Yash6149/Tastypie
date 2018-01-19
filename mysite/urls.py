"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from myapp.urls import v1_api

urlpatterns = [
    # The normal jazz here...
    url('admin/', admin.site.urls),
    url(r'^api/',include(v1_api.urls)),
    url(r'^api/myapp/doc/',
        include('tastypie_swagger.urls',
                namespace='myapp_tastypie_swagger'),
        kwargs={"tastypie_api_module": "myapp.urls.v1_api",
                "namespace": "myapp_tastypie_swagger"}),
]

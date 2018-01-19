from django.contrib import admin
from django.conf.urls import url, include
from tastypie.api import Api
from myapp.api import EntryResource, UserResource
v1_api = Api(api_name='v1')

v1_api.register(UserResource())
v1_api.register(EntryResource())
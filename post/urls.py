from django.conf.urls import url

from django.urls import include, path
from .views import *
from . import views


urlpatterns = [
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),

]

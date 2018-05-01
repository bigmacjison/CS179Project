from django.urls import path
from django.conf.urls import url
from AniModels import views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^pet/$', views.PetList.as_view()),
    url(r'^pet/(?P<pk>[0-9]+)/$', views.PetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
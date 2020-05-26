from django.conf.urls import url
from . import views
from .views import (PostListAPIView, PostDetailAPIView, PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView)


urlpatterns = [
    url(r'^$',PostListAPIView.as_view(),name='list' ),
    url(r'^create/',PostCreateAPIView.as_view(), name='create' ),
    url(r'^(?P<id>\d+)/$',PostDetailAPIView.as_view() , name='detail'),
    url(r'^(?P<id>\d+)/edit/$',PostUpdateAPIView.as_view() , name='update'),
    url(r'^(?P<id>\d+)/delete/$',PostDeleteAPIView.as_view() , name='delete'),
    ]

from django.conf.urls import url
from .views import (
    BlogListAPIView,
    BlogDetailAPIView,
    BlogDeleteAPIView,
    BlogUpdateAPIView,
    BlogCreateAPIView,
)

urlpatterns = [

    # /api/blogs

    url(r'^$', BlogListAPIView.as_view(), name='list'),
    url(r'^create$', BlogCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BlogUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BlogDeleteAPIView.as_view(), name='delete'),

]

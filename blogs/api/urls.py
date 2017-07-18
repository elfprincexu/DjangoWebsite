from django.conf.urls import url
from .views import (
    BlogListAPIView,
    BlogDetailAPIView,
    BlogDeleteAPIView,
    BlogUpdateAPIView,
)

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', BlogDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', BlogUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', BlogDeleteAPIView.as_view(), name='delete'),

]

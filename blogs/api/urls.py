from django.conf.urls import url
from .views import (
    BlogListAPIView,
    BlogDetailAPIView,
)

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='list'),

    url(r'^(?P<pk>\d+)/$', BlogDetailAPIView.as_view(), name='detail'),

]

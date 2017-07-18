from django.conf.urls import url
from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
)

urlpatterns = [

    # /api/comments

    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^(?P<id>[\w-]+)/$', CommentDetailAPIView.as_view(), name='thread'),

]

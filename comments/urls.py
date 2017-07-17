from django.conf.urls import url
from .views import comments_thread, comment_delete



urlpatterns = [
    # namespace == comments

    # view
    url(r'^(?P<id>\d+)/$', comments_thread, name="comments_thread"),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name="comment_delete"),

]
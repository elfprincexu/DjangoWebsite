from django.conf.urls import url
from .views import blog_details_by_id, blog_details_by_slug, blogs_home, blog_create,blog_edit_by_id, blog_edit_by_slug, blog_delete_by_id, blog_delete_by_slug
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # namespace == blogs
    # /blogs/
    url(r'^$', blogs_home, name="blogs_index"),

    # create
    url(r'^create/$', blog_create, name="blog_create"),

    # view
    url(r'^(?P<blog_id>\d+)/$', blog_details_by_id, name="blog_details_by_id"),
    url(r'^(?P<blog_slug>[\w-]+)/$', blog_details_by_slug, name="blog_details_by_slug"),

    # edit
    url(r'^(?P<blog_id>\d+)/edit/$', blog_edit_by_id, name="blog_edit_by_id"),
    url(r'^(?P<blog_slug>[\w-]+)/edit/$', blog_edit_by_slug, name="blog_edit_by_slug"),

    # delete
    url(r'^(?P<blog_id>\d+)/delete/$', blog_delete_by_id, name="blog_delete_by_id"),
    url(r'^(?P<blog_slug>[\w-]+)/delete/$', blog_delete_by_slug, name="blog_delete_by_slug"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
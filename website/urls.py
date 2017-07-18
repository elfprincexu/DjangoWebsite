"""posts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

# from src.blogs.views import blogs_home, blog_details
from blogs.views import blogs_home


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^blogs/$', blogs_home, name = "blogs_index"),
    # url(r'^blogs/(?P<blog_id>\w+)/$', blog_details, name = "blog_detail")
    url(r'^blogs/', include('blogs.urls', namespace="blogs")),
    url(r'^api/blogs/', include('blogs.api.urls', namespace="blogs-api")),
    url(r'^api/comments/', include('comments.api.urls', namespace="comments-api")),

    url(r'^comments/', include('comments.urls', namespace="comments")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),


    url(r'^$', blogs_home)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

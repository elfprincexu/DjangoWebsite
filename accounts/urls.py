from django.conf.urls import url
from .views import login_view, logout_view, register_view

urlpatterns = [
    # namespace == comments

    # view
    url(r'^login/$', login_view, name="login_view"),
    url(r'^register/$', register_view, name="register_view"),
    url(r'^logout/$', logout_view, name="logout_view"),
]

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
)

from blogs.models import Blog
from blogs.api.serializers import BlogSerializer, BlogDetailSerializer,BlogCreateSerializer

class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"

class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"


class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # def get_serializer_class(self):

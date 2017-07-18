from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)

from blogs.models import Blog
from blogs.api.serializers import BlogSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # def get_serializer_class(self):


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

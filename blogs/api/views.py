from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from .pagination import BlogLimitOffsetPagination,BlogPageNumberPagination
from .permissions import IsOwnerOrReadyOnly

from blogs.models import Blog
from blogs.api.serializers import BlogListSerializer, BlogDetailSerializer, BlogCreateSerializer


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"


class BlogUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"

    permission_classes = [IsOwnerOrReadyOnly]


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = "slug"


class BlogListAPIView(ListAPIView):
    # queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['title','content','author__first_name', 'author__last_name']
    ordering_fields = ['title','updated']
    pagination_class = BlogPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(BlogListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Blog.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__first_name__icontains=query) |
                Q(author__last_name__icontains=query)
            ).distinct()
        return queryset_list

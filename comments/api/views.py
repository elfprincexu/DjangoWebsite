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

from blogs.api.pagination import BlogLimitOffsetPagination, BlogPageNumberPagination
from blogs.api.permissions import IsOwnerOrReadyOnly

from comments.models import Comment
from comments.api.serializers import CommentDetailSerializer



class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "id"



class CommentListAPIView(ListAPIView):
    # queryset = Blog.objects.all()
    serializer_class = CommentDetailSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [ 'content', 'user__first_name', 'user__last_name']
    ordering_fields = ['updated']
    pagination_class = BlogPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(BlogListAPIView,self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query)
            ).distinct()
        return queryset_list

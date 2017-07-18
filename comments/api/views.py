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
from comments.api.serializers import CommentSerializer, CommentDetailSerializer, create_comment_serializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = CommentDetailSerializer
    # lookup_field = 'id'
    # lookup_url_kwarg = "id"
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
            model_type=model_type,
            slug=slug,
            parent_id=parent_id,
            user=self.request.user
        )


class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = "id"


class CommentListAPIView(ListAPIView):
    # queryset = Blog.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name', 'user__last_name']
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

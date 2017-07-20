from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class CommentLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class CommentPageNumberPagination(PageNumberPagination):
    page_size = 5
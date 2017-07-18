from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.models import Comment


class CommentDetailSerializer(ModelSerializer):
    class Meta:
        model = Comment

        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
            'parent',
        ]


class CommentListSerializer(ModelSerializer):




    class Meta:
        model = Comment

        fields = [
            'user',
            'object_id',
            'content',
            'parent',

        ]

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.models import Comment


class CommentSerializer(ModelSerializer):

    replies_count = SerializerMethodField()

    def get_replies_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            # 'content_object',
            'parent',
            'content',
            'replies_count',
            'timestamp',
        ]


class CommentChildSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'parent',

        ]

class CommentDetailSerializer(ModelSerializer):
    replies_count = SerializerMethodField()
    replies = SerializerMethodField()

    def get_replies_count(self,obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    class Meta:
        model = Comment

        fields = [
            'user',
            'object_id',
            'content',
            'replies_count',
            'replies',
            'timestamp',
        ]
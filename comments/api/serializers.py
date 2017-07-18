from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
)
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from comments.models import Comment

User = get_user_model()


def create_comment_serializer(model_type='blog', slug=None, parent_id=None, user=None):
    class CommentCreateSerailizer(ModelSerializer):
        class Meta:
            model = Comment
            fields = [
                'id',
                'parent',
                'content',
                'timestamp',
            ]

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            self.slug = slug
            self.parent_obj = None
            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    self.parent_obj = parent_qs.first()
            return super(CommentCreateSerailizer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_qs = ContentType.objects.filter(model=model_type)
            if not model_qs.exists() or model_qs.count() != 1:
                raise ValidationError("This is not a valid model_type ")
            someModel = model_qs.first().model_class()
            obj_qs = someModel.objects.filter(slug=self.slug)
            if not obj_qs.exists() or obj_qs.count() != 1:
                raise ValidationError("This is not a slug for this content type")
            return data

        def create(self, validated_data):
            content = validated_data.get("content")
            if user:
                main_user = user
            else:
                main_user = User.objects.all().first()
            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj
            comment = Comment.objects.create_by_model_type(
                model_type,
                slug,
                content,
                main_user,
                parent_obj
            )
            return comment

    return CommentCreateSerailizer


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

    def get_replies_count(self, obj):
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

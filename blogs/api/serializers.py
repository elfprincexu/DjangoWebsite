from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from blogs.models import Blog

from comments.api.serializers import CommentSerializer
from comments.models import Comment


class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog

        fields = [
            'title',
            'content',
            'updated',
        ]


class BlogListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='blogs-api:detail',
        lookup_field='slug',
    )

    delete_url = HyperlinkedIdentityField(
        view_name='blogs-api:delete',
        lookup_field='slug',
    )

    author = SerializerMethodField()

    coverimg = SerializerMethodField()


    def get_author(self, obj):
        return str(obj.author.username)

    def get_coverimg(self,obj):
        try:
            image = obj.coverimg.url
        except:
            image = None
        return image

    class Meta:
        model = Blog

        fields = [
            'url',
            'delete_url',
            'title',
            'author',
            'content',
            'updated',
            'coverimg',
        ]


class BlogDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    coverimg = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    def get_comments(self,obj):
        content_type = obj.get_content_type
        obj_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        return CommentSerializer(c_qs, many= True).data


    def get_author(self, obj):
        return str(obj.author.username)

    def get_coverimg(self, obj):
        try:
            image = obj.coverimg.url
        except:
            image = None
        return image

    def get_html(self,obj):
        return obj.get_mark_down()

    class Meta:
        model = Blog

        fields = [
            'id',
            'title',
            'author',
            'slug',
            'content',
            'html',
            'updated',
            'coverimg',
            'comments',
        ]


"""

from blogs.models import Blog
from blogs.api.serializers import BlogDetailSerializer

data = {
    'title' : 'hello serializer',
    "author" : 1 ,
    "content" : 'hello serializer',
    'updated' : '2017-07-17'
    }
    
obj = Blog.objects.get(id=3)
    
new_item = BlogDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print (new_item.errors)
    
"""

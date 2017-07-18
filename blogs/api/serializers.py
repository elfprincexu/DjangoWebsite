from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from blogs.models import Blog


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

    class Meta:
        model = Blog

        fields = [
            'url',
            'delete_url',
            'title',
            'author',
            'content',
            'updated',
        ]


class BlogDetailSerializer(ModelSerializer):
    class Meta:
        model = Blog

        fields = [
            'id',
            'title',
            'author',
            'slug',
            'content',
            'updated',
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

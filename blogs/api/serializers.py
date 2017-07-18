from rest_framework.serializers import ModelSerializer

from blogs.models import Blog


class BlogCreateSerializer(ModelSerializer):
    class Meta:
        model = Blog

        fields = [
            'title',
            # 'author',
            # 'slug',
            'content',
            'updated',
        ]

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog

        fields = [
            'title',
            'author',
            'slug',
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
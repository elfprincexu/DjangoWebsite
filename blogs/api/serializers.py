from rest_framework.serializers import ModelSerializer

from blogs.models import Blog

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
data = {
    'title' : 'hello serializer',
    "author" : 1 ,
    "content" : 'hello serializer',
    'updated' : '2017-07-17'
    }
    
new_item = BlogSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print (new_item.errors)
    
"""
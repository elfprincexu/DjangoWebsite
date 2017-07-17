from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator, get_read_time
from django.urls import reverse
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from markdown_deux import markdown


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        app_label = "blogs"


def upload_location(instance, filename):
    return "{0}/{1}".format(instance.id, filename)


class Blog(models.Model):
    # Blog content: title, author, context
    title = models.CharField(max_length=120)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    # Blog slug url for better
    slug = models.SlugField(blank=True, unique=True)
    # Blog viewsCount
    viewedCount = models.IntegerField(default=0, editable=False)
    # Blog cover Image
    coverimg = models.ImageField(upload_to=upload_location, null=True, blank=True)

    # timestamps of creation and updated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    readtime = models.TimeField(null=True, blank=True)

    # for admin
    def __str__(self):
        return self.title

    # this will be used for rediect with a model
    def get_absolute_url(self):
        return reverse('blogs:blog_details_by_slug', args=[self.slug])

    def get_mark_down(self):
        marked_content = markdown(self.content)
        return mark_safe(marked_content)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance)
        return content_type

    class Meta:
        ordering = ["-updated", "-created"]
        app_label = "blogs"


_UNSAVED_IMAGEFIELD = 'unsaved_coverimg'


# define this pre_save, to do something before save() method
def pre_save_blog_receiver(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = unique_slug_generator(instance)

    if instance.content:
        read_time = get_read_time(instance.get_mark_down())
        instance.readtime = read_time

    if not instance.pk and not hasattr(instance, _UNSAVED_IMAGEFIELD):
        setattr(instance, _UNSAVED_IMAGEFIELD, instance.coverimg)
        instance.coverimg = None


def post_save_blog_image_receiver(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_IMAGEFIELD):
        instance.coverimg = getattr(instance, _UNSAVED_IMAGEFIELD)
        instance.save()


# register the signal and the receiver
pre_save.connect(pre_save_blog_receiver, sender=Blog)

post_save.connect(post_save_blog_image_receiver, sender=Blog)

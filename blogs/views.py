from urllib.parse import quote_plus

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.contrib.contenttypes.models import ContentType

from .form import BlogForm
from .models import Blog
from .utils import get_read_time

from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.



# blogs_home_index
def blogs_home(request, *args, **kwargs):
    query = request.GET.get("q")
    if query:
        blogs_set = get_list_or_404(Blog,
                                    Q(title__icontains=query) |
                                    Q(content__icontains=query) |
                                    Q(author__first_name__icontains=query) |
                                    Q(author__last_name__icontains=query)
                                    )
    else:
        blogs_set = get_list_or_404(Blog)

    paginator = Paginator(blogs_set, 5)  # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)

    return render(request, "blogs/blogs_home.html", {'blogs': blogs})


# blog create
def blog_create(request, *args, **kwargs):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # process the form data
            blog = form.save()

            # return HttpResponseRedirect (reverse("blogs:blog_details_by_slug", args=[blog.slug]))
            return redirect(blog)
    else:
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, "blogs/blog_form.html", context)


# blog details
def blog_details_by_id(request, blog_id=None, *args, **kwargs):
    blog = get_object_or_404(Blog, id=blog_id)
    shared_string = quote_plus(blog.content)

    read_time = get_read_time(blog.content)

    initial_data = {
        "content_type": blog.get_content_type,
        "object_id": blog.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id = parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    # comments = Comment.objects.filter_by_instance(blog)
    comments = blog.comments

    # the blog retrieved with success
    if isinstance(blog, Blog):
        blog.viewedCount += 1
        blog.save()  # do not forget to save it
    context = {
        "blog": blog,
        "shared_string": shared_string,
        "comments": comments,
        "comments_form": form,
    }
    return render(request, "blogs/blog_details.html", context)


def blog_details_by_slug(request, blog_slug=None, *args, **kwargs):
    blog = get_object_or_404(Blog, slug=blog_slug)
    shared_string = quote_plus(blog.content)

    initial_data = {
        "content_type": blog.get_content_type,
        "object_id": blog.id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        parent_obj = None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id = None
        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content_data,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

    # comments = Comment.objects.filter_by_instance(blog)
    comments = blog.comments

    # the blog retrieved with success
    if isinstance(blog, Blog):
        blog.viewedCount += 1
        blog.save()  # do not forget to save it
    context = {
        "blog": blog,
        "shared_string": shared_string,
        "comments": comments,
        "comments_form": form,
    }
    return render(request, "blogs/blog_details.html", context)


# blogs edit
def blog_edit_by_id(request, blog_id, *args, **kwargs):
    # edit current instance
    if request.method == 'GET':
        blog = get_object_or_404(Blog, id=blog_id)
        if isinstance(blog, Blog):  # get that blog
            form = BlogForm(instance=blog)
            context = {
                'form': form
            }
        return render(request, 'blogs/blog_form.html', context)
    # update current instance
    else:
        blog = get_object_or_404(Blog, id=blog_id)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
        return redirect(blog)


def blog_edit_by_slug(request, blog_slug, *args, **kwargs):
    # edit current instance
    if request.method == 'GET':
        blog = get_object_or_404(Blog, slug=blog_slug)
        if isinstance(blog, Blog):  # get that blog
            form = BlogForm(instance=blog)
            context = {
                'form': form
            }
        return render(request, 'blogs/blog_form.html', context)
    # update current instance
    else:
        blog = get_object_or_404(Blog, slug=blog_slug)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save()
        return redirect(blog)


# blog delete
def blog_delete_by_id(request, blog_id, *args, **kwargs):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()

    return HttpResponseRedirect(reverse('blogs:blogs_index'))


def blog_delete_by_slug(request, blog_slug, *args, **kwargs):
    blog = get_object_or_404(Blog, slug=blog_slug)
    blog.delete()

    return HttpResponseRedirect(reverse('blogs:blogs_index'))

from django.shortcuts import render, get_object_or_404

from .models import Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()       #setting LOGIN_URL
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)

    # add permission check
    if request.user != comment.user:
        response = HttpResponse(" you don't have the permissions to do this !")
        response.status_code = 403
        return response

    if request.method == "POST":
        parent_obj_url = comment.content_object.get_absolute_url()
        comment.delete()
        return HttpResponseRedirect(parent_obj_url)

    context = {
        "comment" : comment,
    }

    return render(request,"comments/comment_delete.html", context)


def comments_thread(request, id):
    comment = get_object_or_404(Comment, id=id)

    initial_data = {
        "content_type": comment.content_type,  # blog that the comment is on
        "object_id": comment.object_id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)

    if form.is_valid() and request.user.is_authenticated():
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

    context = {
        "comment": comment,
        "form": form
    }
    return render(request, "comments/comments_thread.html", context)

"""
Views for the posts app.
Handles displaying, creating, updating, and deleting posts.
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(generic.ListView):
    """
    Display a list of published posts.
    """
    queryset = Post.objects.filter(
        status=1,
        approved=True
    ).order_by("-created_on")
    template_name = "posts/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Renders the details of a specific post and allows users to interact with
    the post form.

    Displays an individual instance of model :model:`Post`.

    **Context**
    - ``post``: The selected instance of :model:`Post`, retrieved by slug.
    - ``posts_form``: The form rendered by this view (form: `PostForm`).

    Returns the template: *posts/post_detail.html*
    """
    posts_form = PostForm()
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "posts/post_detail.html",
        {"post": post, "posts_form": posts_form},
    )


@login_required
def create_post(request):
    """
    Renders the post creation form and handles submission of new posts.

    Displays an individual instance of model :model:`Post`.

    **Context**
    - ``form``: The post creation form (form: `PostForm`).

    Returns the template: *posts/create_post.html*
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post is waiting approval!")
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm()

    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,
        },
    )


@login_required
def edit_post(request, post_id):
    """
    Renders the post editing form and handles submission of post updates.

    Displays an individual instance of model :model:`Post`.

    **Context**
    - ``form``: The post editing form (form: `PostForm`).

    Returns the template: *posts/create_post.html*
    """
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        messages.error(
            request, "You do not have permission to edit this post.")
        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            edited_post = form.save(commit=False)
            edited_post.user = request.user
            edited_post.approved = False
            edited_post.save()
            messages.success(request, "Your post is waiting approval!")
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,
        },
    )


def delete_post(request, post_id):
    """
    Handles the deletion of a specific post by the authenticated user.

    Displays an individual instance of model :model:`Post`.

    **Context**
    - ``form``: The post form (form: `PostForm`) for confirmation before
    deletion.

    Returns the template: *posts/create_post.html*
    """
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        messages.error(
            request, "You do not have permission to delete this post.")
        return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
    if request.method == "POST":
        post.delete()
        messages.success(request, "Your post has been deleted.")
        return HttpResponseRedirect(reverse('home'))
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,

        },
    )

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1, approved=True).order_by("-created_on")
    template_name = "posts/index.html"
    paginate_by = 6


def post_detail(request, slug):
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
    View for creating a new post.
    Login is required to access this view.
    """
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post is waiting approval!")
            return reverse('home')
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
    View for editing a new post.
    Login is required to access this view.
    """
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        messages.error(request, "You do not have permission to edit this post.")
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
    View for deleting a post.
    Login is required to access this view.
    """
    post = get_object_or_404(Post, id=post_id)
    if post.user != request.user:
        messages.error(request, "You do not have permission to delete this post.")
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

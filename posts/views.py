from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
            return redirect('home')
    else:
        form = PostForm()

    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,
        },
    )

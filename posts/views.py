from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.afilter(status=1).order_by("created_on")
    template_name = "post_list.html"

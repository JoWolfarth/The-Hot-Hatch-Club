from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("accounts/", include("allauth.urls")),
]

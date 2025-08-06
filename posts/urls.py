from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='posts'),
    path('create/', views.create_post, name='create_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("accounts/", include("allauth.urls")),
    path("edit/<int:post_id>/", views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]

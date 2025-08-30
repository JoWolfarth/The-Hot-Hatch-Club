"""
This module defines the database models for the posts app.
Models:
    - Post: Represents a post about a vehicle, linked to a user.
"""
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"), (2, "Pending"),)


# Create your models here.
class Post(models.Model):
    """
    stores a post about a vehicle related to :model:`User`
    """
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    vehicle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.PositiveIntegerField()
    bhp = models.PositiveIntegerField()
    engine = models.CharField(max_length=25, default="", blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=((0, "Draft"), (1, "Published"),), default=0)
    approved = models.BooleanField(default=False)
    excerpt = models.TextField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically generate a unique
        slug based on the vehicle name if not provided.
        """
        if not self.slug or self.slug == "":
            base_slug = slugify(self.vehicle)
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns a string representation of the post, showing the vehicle name.
        """
        return f"The title of this post is {self.vehicle}"

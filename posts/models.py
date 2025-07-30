from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    vehicle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    year = models.PositiveIntegerField()
    bhp = models.PositiveIntegerField()
    engine_size = models.DecimalField(max_digits=5, decimal_places=2)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

"""
Custom forms for the posts app.
"""

from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """
    Form for creating and updating instances of model :model:`Post`.

    - Includes fields for vehicle details and post content.
    - Used for both post creation and editing in the posts app.
    """
    class Meta:
        model = Post
        fields = (
            'vehicle', 'year', 'bhp', 'engine', 'content', 'status', 'excerpt')

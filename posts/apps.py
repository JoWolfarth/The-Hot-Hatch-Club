from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    Configuration class for the posts app.

    - Sets the default auto field to 'BigAutoField'.
    - Registers the app under the name 'posts'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

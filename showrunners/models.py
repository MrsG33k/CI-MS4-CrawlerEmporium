from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    """ For blogposts by showrunners and admin """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   # noqa: E501
    content = models.TextField()
    summary = models.CharField(max_length=500, help_text="A snippet for the main blog grid page.")   # noqa: E501

    # images for the blogposts
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} | by {self.author.username}"


class BlogComment(models.Model):
    """ Comments only allowed by logged in users """
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')   # noqa: E501
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comments')   # noqa: E501
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

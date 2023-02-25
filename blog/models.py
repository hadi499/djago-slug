from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    class PostPublish(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='publish')

    options = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=20, choices=options, default='draft')
    post_publish = PostPublish()

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth import get_user_model

# Get the User model
User = get_user_model()


# models
class News(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.SET_NULL, null=True, blank=True, related_name="news"
    )

    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=250)
    slug = models.SlugField()
    content = models.TextField()

    views = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # slugify
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Get the User model
User = get_user_model()


# Abstract Base Model for common content fields
class BaseContentModel(models.Model):
    title = models.CharField(max_length=150)
    desc = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    thumbnail = models.ImageField(upload_to="thumbnail/%Y/%m/%d/")
    is_active = models.BooleanField(default=True)

    # Timestamps
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]
        abstract = True

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Category Model
class Category(BaseContentModel):
    class Meta:
        verbose_name_plural = "Categories"


# News Model
class News(BaseContentModel):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news"
    )
    content = models.TextField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="news"
    )

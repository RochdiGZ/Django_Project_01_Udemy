from django.utils.text import slugify
from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField(default="")

    @property
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article n'est pas accessible"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

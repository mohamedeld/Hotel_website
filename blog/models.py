from django.db import models
import datetime
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, related_name='post_author', on_delete=models.CASCADE,verbose_name=_("author"))
    title = models.CharField(max_length=100,verbose_name =_("title"))
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(_('image'),upload_to='post/')
    created_at = models.DateTimeField(_('Created at'),default=datetime.datetime.now)
    category = models.ForeignKey(
        'Category', related_name='post_category', on_delete=models.CASCADE,verbose_name=_("category"))
    tags = TaggableManager()
    description = models.TextField(_('Description'),max_length=15000)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

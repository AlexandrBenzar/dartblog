from django.db import models

"""
Category
=========
title, slug

Tag
=========
title, slug

Post
=========
title, slug, author, content, created_at, photo, quantity_views, category, tags
"""


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='Url', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='Url', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='Url', max_length=255, unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(verbose_name='Опубликовано', auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    quantity_views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    # Сортировка по полю дата создания в обратном порядке
    class Meta:
        ordering = ['-created_at']

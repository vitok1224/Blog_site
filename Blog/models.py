from django.urls import reverse

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, verbose_name='url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tage(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, verbose_name='tag', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tage', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='tag', unique=True)
    author = models.CharField(max_length=25)
    content = models.TextField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tage = models.ManyToManyField('Tage', blank=True, )

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

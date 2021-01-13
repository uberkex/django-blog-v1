from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Kategori')
    image = models.ImageField(upload_to='articles/categories/')
    slug = models.SlugField(unique=True)
    sorting = models.IntegerField(verbose_name='Sıra')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'
        ordering = ['sorting']


# Anlatılacaklar
# ForeignKey / on_delete / related_name / choices / slug

# Taslak - Yayınla
STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


# ImageFonksiyon
def upload_article_image(instance, filename):
    filebase, extension = filename.split('.')
    return '{}/{}.{}'.format('articles', instance.title, extension)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Makale Başlık")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles', verbose_name='Kategori')
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_post", verbose_name="Yazar")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Durum")
    image = models.ImageField(upload_to=upload_article_image, verbose_name='Kapak Resmi')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    # Part2
    class Meta:
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"
        ordering = ['-created_date']

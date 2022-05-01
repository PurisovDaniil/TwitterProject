from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to='users/avatars')
    user_description = models.CharField('Описание пользователя', max_length=150)
    user_nickname = models.CharField('Никнейм пользователя', max_length=30)
    
    class Meta:
        verbose_name = 'Дополнительное поле пользователя'
        verbose_name_plural = 'Дополнительные поля пользователя'
    
    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField('Картинка', upload_to='image/')
    title = models.CharField('Заголовок', max_length=100)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('Ссылка', unique=True)
    image = models.ImageField('Картинка', blank=True, null=True)

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_link(self):
        return reverse('category_detail_url', kwargs = {'slug':self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    users = models.ManyToManyField(User, related_name = 'favourite_posts')
    date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

# class Post(models.Model):
#     slug = models.SlugField('Ссылка', max_length=150, unique=True)
#     text = models.TextField('Текст', blank=True, null=True)
#     date = models.DateTimeField('Дата', default=0)
#     author = models.CharField('Автор', max_length=20)

#     def get_link(self):
#         return reverse('')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to='users/avatars')
    
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


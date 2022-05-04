from django.db import models
from django.shortcuts import reverse


# Create your models here.

class Post(models.Model):
    slug = models.SlugField('Ссылка', max_length=150, unique=True)
    text = models.TextField('Текст', blank=True, null=True)
    date = models.DateTimeField('Дата', default=0)
    author = models.CharField('Автор', max_length=20)

    def get_link(self):
        return reverse('')
        
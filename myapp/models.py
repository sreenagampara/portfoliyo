from django.db import models


# Create your models here.

class home(models.Model):
    logo_image = models.CharField(max_length=2000)
    author_image = models.CharField(max_length=2000, default='Null')
    author_about = models.CharField(max_length=200, default='Null')
    bg_image = models.CharField(max_length=2000, default='Null')
    objects = models.Manager()


class about(models.Model):
    author_detail1 = models.CharField(max_length=1000, default='Null')
    author_detail2 = models.CharField(max_length=1000, default='Null')
    author_detail3 = models.CharField(max_length=1000, default='Null')
    author_detail4 = models.CharField(max_length=1000, default='Null')
    author_detail5 = models.CharField(max_length=1000, default='Null')
    author_detail6 = models.CharField(max_length=1000, default='Null')
    author_detail7 = models.CharField(max_length=1000, default='Null', blank=True)
    author_detail8 = models.CharField(max_length=1000, default='Null', blank=True)
    author_detail9 = models.CharField(max_length=1000, default='Null', blank=True)
    author_detail10 = models.CharField(max_length=1000, default='Null', blank=True)
    page_image = models.CharField(max_length=2000, default='Null', blank=True)
    bg_image = models.CharField(max_length=2000, default='Null', blank=True)
    objects = models.Manager()

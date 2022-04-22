from django.db import models


# Create your models here.

class home(models.Model):
    logo_image = models.CharField(max_length=2000)
    author_image = models.CharField(max_length=2000, default='Null')
    author_about = models.CharField(max_length=200, default='Null')
    bg_image = models.CharField(max_length=2000, default='Null')
    objects = models.Manager()


class about(models.Model):
    author_detail = models.CharField(max_length=1000, default='Null')
    page_image = models.CharField(max_length=2000, default='Null')
    bg_image = models.CharField(max_length=2000, default='Null')
    objects = models.Manager()

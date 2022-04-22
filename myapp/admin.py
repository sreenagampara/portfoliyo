from django.contrib import admin
from .models import home, about


class homeadmin(admin.ModelAdmin):
    list_display = ('logo_image', 'author_image', 'author_about', 'bg_image')


class aboutadmin(admin.ModelAdmin):
    list_display = ('author_detail1', 'author_detail2', 'author_detail3',
                    'author_detail4', 'author_detail5', 'author_detail6',
                    'author_detail7', 'author_detail8', 'author_detail9',
                    'author_detail10', 'page_image', 'bg_image')


# Register your models here.
admin.site.register(home, homeadmin)
admin.site.register(about, aboutadmin)

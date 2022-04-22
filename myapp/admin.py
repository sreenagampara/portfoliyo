from django.contrib import admin
from .models import home, about


class homeadmin(admin.ModelAdmin):
    list_display = ('logo_image', 'author_image', 'author_about', 'bg_image')

class aboutadmin(admin.ModelAdmin):
    list_display = ('author_detail', 'page_image', 'bg_image')


# Register your models here.
admin.site.register(home, homeadmin)
admin.site.register(about, aboutadmin)

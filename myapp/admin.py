from django.contrib import admin
from .models import home, about, resume, project, contact, map


class homeadmin(admin.ModelAdmin):
    list_display = ('logo_image', 'author_image', 'author_about', 'bg_image')


class aboutadmin(admin.ModelAdmin):
    list_display = ('author_detail1', 'author_detail2', 'author_detail3',
                    'author_detail4', 'author_detail5', 'author_detail6',
                    'author_detail7', 'author_detail8', 'author_detail9',
                    'author_detail10', 'page_image', 'bg_image')


class resumeadmin(admin.ModelAdmin):
    list_display = ('author_resume1', 'author_resume2', 'author_resume3', 'bg_image')


class projectadmin(admin.ModelAdmin):
    list_display = ('project_link', 'project_image', 'project_head1', 'project_head2')


class contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class mapadmin(admin.ModelAdmin):
    list_display = ('map',)


# Register your models here.
admin.site.register(home, homeadmin)
admin.site.register(about, aboutadmin)
admin.site.register(resume, resumeadmin)
admin.site.register(project, projectadmin)
admin.site.register(contact, contactadmin)
admin.site.register(map, mapadmin)

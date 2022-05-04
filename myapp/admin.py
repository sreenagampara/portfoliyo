from django.contrib import admin
from .models import home, about, resume_experience, project, contact, map, resume_education, resume_contact, resume_skill


class homeadmin(admin.ModelAdmin):
    list_display = ('logo_image', 'author_image', 'author_about', 'bg_image')


class aboutadmin(admin.ModelAdmin):
    list_display = ('author_detail1', 'author_detail2', 'author_detail3',
                    'author_detail4', 'author_detail5', 'author_detail6',
                    'author_detail7', 'author_detail8', 'author_detail9',
                    'author_detail10', 'page_image', 'bg_image')


class resume_experienceadmin(admin.ModelAdmin):
    list_display = ('job', 'company', 'details', 'bg_image', 'from_year', 'to_year')


class projectadmin(admin.ModelAdmin):
    list_display = ('project_link', 'project_image', 'project_head1', 'project_head2', 'bg_image')


class contactadmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class mapadmin(admin.ModelAdmin):
    list_display = ('map', 'bg_image')


class resume_educationadmin(admin.ModelAdmin):
    list_display = ('course', 'institute', 'details')


class resume_skilladmin(admin.ModelAdmin):
    list_display = ('skill', )

class resume_contactadmin(admin.ModelAdmin):
    list_display = ('symbol', 'link', 'detail')


# Register your models here.
admin.site.register(home, homeadmin)
admin.site.register(about, aboutadmin)
admin.site.register(resume_experience, resume_experienceadmin)
admin.site.register(project, projectadmin)
admin.site.register(contact, contactadmin)
admin.site.register(map, mapadmin)
admin.site.register(resume_education, resume_educationadmin)
admin.site.register(resume_skill, resume_skilladmin)
admin.site.register(resume_contact, resume_contactadmin)
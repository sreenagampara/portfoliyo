from django.shortcuts import render
from .models import home, about, resume, project


# Create your views here.
def index(request):
    data = home.objects.all()
    about_data = about.objects.all()
    resume_data = resume.object.all()
    project_data = project.object.all()
    context = {
        'datas': data,
        'about_datas': about_data,
        'resume_datas': resume_data,
        'project_datas': project_data
    }
    return render(request, 'index.html', context)

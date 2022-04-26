from django.shortcuts import render
from .models import home, about, resume, project, map, contact


# Create your views here.
def index(request):
    data = home.objects.all()
    about_data = about.objects.all()
    resume_data = resume.object.all()
    project_data = project.object.all()
    mymap = map.object.all()
    context = {
        'datas': data,
        'about_datas': about_data,
        'resume_datas': resume_data,
        'project_datas': project_data,
        'map': mymap
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.object.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'index.html', context)

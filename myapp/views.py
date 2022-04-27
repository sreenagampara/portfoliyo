from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
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
        'map': mymap,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.object.create(name=name, email=email, subject=subject, message=message)

        subjects = subject
        n = '/n'
        messages = f'{name}{chr(10)} {email}{chr(10)} {message}'
        email = 'sree.nagampara@gmail.com'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subjects, messages, email_from, recipient_list)

    return render(request, 'index.html', context)

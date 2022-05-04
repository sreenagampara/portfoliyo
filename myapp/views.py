from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import home, about, resume_experience, project, map, contact, resume_education, resume_contact, resume_skill


# Create your views here.
def index(request):
    data = home.objects.all()
    about_data = about.objects.all()
    resume_data = resume_experience.object.all()
    project_data = project.object.all()
    mymap = map.object.all()
    resume_data1 = resume_education.object.all()
    resume_skills = resume_skill.object.all()
    resume_contacts = resume_contact.object.all()

    context = {
        'datas': data,
        'about_datas': about_data,
        'resume_datas': resume_data,
        'project_datas': project_data,
        'map': mymap,
        'resume_datas1': resume_data1,
        'resume_skill': resume_skills,
        'resume_contact': resume_contacts
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.object.create(name=name, email=email, subject=subject, message=message)

        subjects = subject
        messages = f'{name}{chr(10)} {email}{chr(10)} {message}'
        email = 'sree.nagampara@gmail.com'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(subjects, messages, email_from, recipient_list)

    return render(request, 'index.html', context)

from django.shortcuts import render
from .models import home, about


# Create your views here.
def index(request):
    data = home.objects.all()
    about_data = about.objects.all()
    context = {
        'datas': data,
        'about_datas': about_data
    }
    return render(request, 'index.html', context)

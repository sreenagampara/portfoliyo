from django.shortcuts import render
from .models import home


# Create your views here.
def index(request):
    data = home.objects.all()
    return render(request, 'index.html', {'datas': data})

import datetime
from django.shortcuts import render
from .models import Vacancy


def home_page(request):
    date = datetime.datetime.now().date()
    user = 'Akbar'

    qs = Vacancy.objects.all()

    _context = {'date': date, 'user': user, 'object_list': qs}

    return render(request, 'scraping/home.html', _context)

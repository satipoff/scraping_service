from django.shortcuts import render
import datetime


def home_page(request):
    date = datetime.datetime.now().date()
    user = 'Akbar'

    _context = {'date': date, 'user': user}

    return render(request, 'scraping/home.html', _context)

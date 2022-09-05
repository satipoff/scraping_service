import datetime
from django.shortcuts import render
from .models import Vacancy


def home_page(request):
    date = datetime.datetime.now().date()
    user = 'Akbar'

    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []

    if city or language:
        _filter = {}
        if city:
            _filter['city__name'] = city
        if language:
            _filter['language__name'] = language

        qs = Vacancy.objects.filter(**_filter)

    _context = {'date': date, 'user': user, 'object_list': qs}

    return render(request, 'scraping/home.html', _context)

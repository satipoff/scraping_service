import datetime
from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy


def home_page(request):

    form = FindForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs = []

    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

        qs = Vacancy.objects.filter(**_filter)

    _context = {'object_list': qs, 'form': form}

    return render(request, 'scraping/home.html', _context)

from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open ('pagination\data-398-2018-08-30.csv',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        content = [str(i) for i in reader]
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(content, 10)
        page = paginator.get_page(page_number)


    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)

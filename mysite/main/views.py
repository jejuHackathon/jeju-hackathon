from django.shortcuts import render, redirect
from .models import Oreum


def index(request):
    context = {
        'locations' : Oreum.locations
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def list(request):

    selected_locations = request.GET.getlist('locations')
    search = request.GET.get('search')

    if selected_locations:
        oreums = Oreum.objects.filter(locationin=selected_locations)
    elif search:
        oreums = Oreum.objects.filter(nameicontains=search)
    else:
        oreums = Oreum.objects.all()

    context = {
        'oreums': oreums
    }

    return render(request, 'main/list.html', context)


def detail(request):
    # oreum = Oreum.objects.get(pk=pk)

    # context = {
    #     'oreum': oreum,
    # }

    return render(request, 'main/detail.html')


def create(request):
    if request.method == 'POST':

        data = {
            'name': request.POST.get('name'),
            'location': request.POST.get('location'),
            'phone': request.POST.get('phone'),
            'insta': request.POST.get('insta'),
            'content': request.POST.get('content'),
            'mainphoto': request.FILES.get('mainphoto'),
            'subphoto': request.FILES.get('subphoto'),
        }

        oreum = Oreum.objects.create(**data)

        return redirect(f'/oreumlist/{oreum.pk}/')

    context = {
        'locations': Oreum.locations,
    }

    return render(request, 'main/create.html', context)

from django.shortcuts import render, redirect
from .models import Oreum


def index(request):
    context = {
        'locations' : Oreum.locations
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def oreumlist(request):
    
    selected_locations = request.GET.getlist('locations')
    search = request.GET.get('search')
    
    if selected_locations:
        oreums = oreum.objects.filter(location__in=selected_locations)
    elif search:
        oreums = oreum.objects.filter(name__icontains=search)
    else:
        oreums = oreum.objects.all()
    
    context = {
        'oreums': oreums
    }
    
    return render(request, 'main/oreumlist.html', context)


def oreumdetails(request, pk):
    oreum = Oreum.objects.get(pk=pk)
    
    context = {
        'oreum': oreum,
    }
    
    return render(request, 'main/oreumdetails.html', context)


def write(request):
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
        
    return render(request, 'main/write.html', context)

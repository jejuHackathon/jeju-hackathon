from django.shortcuts import render, redirect
from .models import Oreum


def index(request):
    
    # 닉네임을 입력 받으면 index 페이지로 이동 
    # if request.method == 'POST':
    return render(request, 'main/index.html')


def home(request):
    context = {
        'locations' : Oreum.locations
    }
    return render(request, 'main/home.html', context)

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


def detail(request, pk):
    oreum = Oreum.objects.get(pk=pk)

    context = {
        'oreum': oreum,
        # context에 nickname값 추가 
        'nickname': request.COOKIES.get('nickname'),
    }

    return render(request, 'main/detail.html', context)


def create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'oreumlevel': request.POST.get('oreumlevel'),
            'nightview' : request.POST.get('nightview'),
            'location': request.POST.get('location'),
            'phone': request.POST.get('phone'),
            'insta': request.POST.get('insta'),
            'content': request.POST.get('content'),
            'mainphoto': request.FILES.get('mainphoto'),
            'subphoto': request.FILES.get('subphoto'),
            # cookie에 저장된 nickname값을 읽어와 nickname 컬럼에 저장
            'nickname': request.COOKIES.get('nickname')
        }

        oreum = Oreum.objects.create(**data)

        return redirect(f'/list/{oreum.pk}/')

    context = {
        'locations': Oreum.locations,
        'oreumlevels': Oreum.oreumlevels,
        'nightviews': Oreum.nightviews
    }

    return render(request, 'main/create.html', context)


def update(request, pk):
  
    if request.method == 'POST':
        oreum = Oreum.objects.get(pk=pk)
        oreum.name = request.POST.get('name')
        oreum.oreumlevel = request.POST.get('oreumlevel')
        oreum.nightview = request.POST.get('nightview')
        oreum.location = request.POST.get('location')
        oreum.phone = request.POST.get('phone')
        oreum.insta = request.POST.get('insta')
        oreum.content = request.POST.get('content')
        # 새로 등록한 이미지가 없다면 변경하지 않음
        if request.FILES.get('mainphoto'):
            oreum.mainphoto = request.FILES.get('mainphoto')
        if request.FILES.get('subphoto'):
            oreum.subphoto = request.FILES.get('subphoto'),
        oreum.save()

        return redirect('/list')

    oreum = Oreum.objects.get(pk=pk)
  
    context = {
        'oreum': oreum,
        'nickname': request.COOKIES.get('nickname'),
        'locations': Oreum.locations,
        'oreumlevels': Oreum.oreumlevels,
        'nightviews': Oreum.nightviews, 
    }
    return render(request, "main/update.html", context)


def delete(request, pk):
    oreum = Oreum.objects.get(pk=pk)
    oreum.delete()
    return redirect('/list')


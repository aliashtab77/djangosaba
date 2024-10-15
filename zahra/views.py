from django.shortcuts import render
from zahra.models import SliderModel

# Create your views here.


def index(request):
    sliders = SliderModel.objects.all()
    context = {
        "slides" :sliders,
    }
    return render(request, 'index.html', context=context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context=context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context=context)


def elements(request):
    context = {

    }
    return render(request, 'elements.html', context=context)


def services(request):
    context = {

    }

    return render(request, 'services.html', context=context)

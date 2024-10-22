from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from zahra.models import SliderModel, Information, PopularDestination, Testimonials, SpecialModel, MessagesModel, HotelModel, Category, BlogModel



# Create your views here.


def index(request):
    sliders = SliderModel.objects.all()
    inf = Information.objects.all()
    tes = Testimonials.objects.all()
    specials = SpecialModel.objects.all()
    pop = PopularDestination.objects.all()
    if inf:
        inf = inf[0]
    context = {
        "slides" :sliders,
        "inf":inf,
        "pop":pop,
        "tes":tes,
        "specials":specials,
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

def savamessageofuser(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        message = request.POST['message']
        mamad = MessagesModel(first_name=firstname, last_name=lastname, phone=phone, message=message)
        mamad.save()
        return HttpResponseRedirect(reverse('contact'))


def hotels(request):
    hotels = HotelModel.objects.all()
    print(hotels[0].star)
    print(type(hotels[0].star))
    context = {
        "hotels":hotels,
        "ra":range(1, 6)
    }
    return render(request, 'hotels.html', context=context)

def blogs(request):
    blogs = BlogModel.objects.all()
    categories = Category.objects.all()
    p = Paginator(blogs, 2)
    page = request.GET.get('page', 1)
    pages = p.page(page)
    context = {
        "cats":categories,
        "blogs":pages,
        "p":p
    }
    return render(request, 'blogs.html', context=context)

def blogs_details(request, id):
    blogs = BlogModel.objects.get(id=id)
    context = {
        "blog":blogs,
    }
    return render(request, 'blog-single.html', context=context)
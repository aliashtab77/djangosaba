from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, FileResponse, Http404
from django.urls import reverse
from django.core.paginator import Paginator
from zahra.models import SliderModel, Information, PopularDestination, Testimonials, SpecialModel, MessagesModel, HotelModel, Category, BlogModel, VisaDestination, SiteMapModel
# Create your views here.


def index(request):
    sliders = SliderModel.objects.all()
    inf = Information.objects.all()
    tes = Testimonials.objects.all()
    specials = SpecialModel.objects.all()
    pop = PopularDestination.objects.all()
    visa = VisaDestination.objects.all()
    if inf:
        inf = inf[0]
    context = {
        "slides" :sliders,
        "inf":inf,
        "pop":pop,
        "visas": visa,
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
    context = {
        "hotels":hotels,
        "ra":range(1, 6)
    }
    return render(request, 'hotels.html', context=context)

def blogs(request):
    blogs = BlogModel.objects.filter(published=True)
    categories = Category.objects.all()
    p = Paginator(blogs, 9)
    page = request.GET.get('page', 1)
    pages = p.page(page)
    context = {
        "cats":categories,
        "blogs":pages,
        "p":p
    }
    return render(request, 'blogmah.html', context=context)

def blogs_details(request, slug):
    blogs = BlogModel.objects.get(slug=slug)
    tags = blogs.tags.split(",")
    context = {
        "blog":blogs,
        "tags":tags,
        "schema":blogs.get_article_schema(request)
    }

    return render(request, 'blog-singlemah.html', context=context)

def sitemap_view(request, slug):
    sitemap_obj = get_object_or_404(SiteMapModel, slug=slug)
    try:
        file_handle = sitemap_obj.file.open('rb')

        # استفاده از FileResponse بهترین گزینه برای فایل‌های استاتیک است
        # حتما content_type را application/xml ست کنید
        response = FileResponse(file_handle, content_type='application/xml')

        # این خط باعث می‌شود مرورگر فایل را دانلود نکند و مستقیما نمایش دهد
        response['Content-Disposition'] = 'inline'

        return response
    except FileNotFoundError:
        raise Http404("فایل فیزیکی یافت نشد.")
"""
URL configuration for sabadjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from zahra.views import index, about,contact,elements,services, savamessageofuser, hotels, blogs, blogs_details


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('services/', services, name='services'),
    path('messagefromuser/', savamessageofuser, name='savamessageofuser' ),
    path('hotels/', hotels, name='hotels'),
    path('blogs/', blogs, name='blogs'),
    # path('blogs/<int:id>', blogs_details, name='blogs_details'),
    re_path(r'blog/(?P<slug>[^/]+)/?$', blogs_details, name='blogs_details')
]


if settings.IS_DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]
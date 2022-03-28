"""RedirectView_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from school_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='school/home.html')),
    path('home/',views.RedirectView.as_view(url = '/'),name='home'),
    path('google/',views.RedirectView.as_view(url = 'https://www.google.com'),name='google'),
    #path('geekyshows/',views.RedirectView.as_view(url = 'https://www.geekyshows.com'),name='go_to_geeky'),
    path('geekyshows/',views.childRedict.as_view(),name='geek'),
]

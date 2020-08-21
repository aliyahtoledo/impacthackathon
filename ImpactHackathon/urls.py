"""ImpactHackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.conf.urls import url

from ImpactHackathon import settings

app_name = 'ImpactHackathon'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^dashboard/$', views.dashboardView, name='dashboard'),
    url(r'^averageprice/$', views.avgPriceView, name='avgprice'),
    url(r'^cropcycle/$', views.cropCycleView, name='cropcycle'),
    url(r'^inventory/$', views.inventoryView, name='inventory'),
    url(r'^salesorders/$', views.salesordersView, name='salesorders'),
    url(r'^invoice/$', views.salesinvoiceView,  name='invoice'),
    url(r'^index/$', views.indexView,  name='index'),
    url(r'^coopdashboard/$', views.coopdashboardView,  name='coopdashboard'),
url(r'^login/$', views.loginView,  name='login'),



]

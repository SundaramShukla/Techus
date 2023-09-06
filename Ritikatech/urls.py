"""Ritikatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
import Recharge.views as eviews
from django_email_verification import urls as mail_urls
from django.contrib.auth import views as auth_views

from django.views.static import serve
from django.conf.urls import include,url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('logout/', eviews.logout_request, name='logout_request'),
    path('', eviews.Home, name='home'),
    path('Loginpage/', eviews.Login_page, name='Loginpage'),
    path('base/', eviews.showBussinessbyApiorport, name='base'),
    path('dashboard/',eviews.showDashboard, name='dashboard'),
    path('masterdistributor/', eviews.masterdistributor, name='masterdistributor'),
    path('distributor/', eviews.distributor, name='distributor'),
    path('retailer/', eviews.retailer, name='retailer'),
    path('whitelabel/', eviews.whitelabel, name='whitelabel'),
    path('apiuser/', eviews.apiuser, name='apiuser'),
    path('employee/', eviews.employee, name='employee'),
    path('deleteduser/', eviews.deleteduser, name='deleteduser'),
    path('switchuser/', eviews.switchuser, name='switchuser'),
    path('setreferral/', eviews.setreferral, name='setreferral'),
    path('bussinessbyoprator/', eviews.bussinessbyoprator, name='bussinessbyoprator'),
    path('bussinessbyportorapi/', eviews.bussinessbyportorapi, name='bussinessbyportorapi'),
    path('bussinessbyuser/', eviews.bussinessbyuser, name='bussinessbyuser'),
    path('addpurchase/', eviews.addpurchase, name='addpurchase'),
    path('addexpense/', eviews.addexpense, name='addexpense'),
    path('addacwallet/', eviews.addacwallet, name='addacwallet'),
    path('ledgerbook/', eviews.ledgerbook, name='ledgerbook'),
    path('daybook/', eviews.daybook, name='daybook'),
    path('userbook/', eviews.userbook, name='userbook'),
    path('signupsetting/', eviews.SignUpSetting, name='signupsetting'),



    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
  ] 

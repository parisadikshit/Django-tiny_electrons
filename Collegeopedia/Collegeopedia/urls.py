"""Collegeopedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from accounts.views import login_view,register_view,logout_view

admin.site.site_header = 'Collegeopedia Admin'
admin.site.site_title = 'Collegeopedia Admin Panel'
admin.site.index_title = 'Welcome to Collegeopedia Admin Panel'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('call/',include('call.urls')),
    path('',include('call.urls'))
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

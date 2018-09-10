"""noise_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from landing import views as landing
from team import views as team
from contact import views as contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing.index, name='home'),
    path('contact/', contact.contact_view, name='contact'),
    path('about/', landing.about_view, name='about'),
    path('projects/', landing.projects_view, name='projects'),
    path('pricing/', landing.pricing_view, name='pricing'),
    path('team/<int:team_mate_id>', team.teammate, name='team_mate'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

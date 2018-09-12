from django.shortcuts import render
from services.models import Service
from customers.models import (
    Customers,CustomersIntro
)
from testimonial.models import (
    Testimonial,TestimonialsIntro
)
from pricing.models import (
    PricePlan,
)

from about.models import About

from projects.models import (Project, ProjectIntro)
from team.models import (TeamMate, TeamIntro)
from .models import Navigation

# Create your views here.

services = Service.objects.all()

customers = Customers.objects.all()
customer_intro = CustomersIntro.objects.filter(active=True).first()

testimonials = Testimonial.objects.all()
testimonial_intro = TestimonialsIntro.objects.filter(active=True).first()

price_plans = PricePlan.objects.all().reverse()

projects = Project.objects.all()
projects_intro = ProjectIntro.objects.filter(active=True).first()

team_mates = TeamMate.objects.all()
team_mates_intro = TeamIntro.objects.filter(active=True).first()

navigation_links = Navigation.objects.filter(for_footer=False).all()
navigation_footer = Navigation.objects.filter(for_footer=True).all()


def index(request):

    projects = Project.objects.all()[:3]
    price_plans = PricePlan.objects.all()[:3]

    contextvar = {
        'text': 'this is text wiitch',
        'services':services,
        'customers': customers,
        'customer_intro': customer_intro,
        'testimonials': testimonials,
        'testimonial_intro': testimonial_intro,
        'price_plans':price_plans,
        'projects': projects,
        'team_mates':team_mates,
        'projects_intro': projects_intro,
        'team_mates_intro': team_mates_intro,
        'navigation_links': navigation_links,
        'navigation_footer': navigation_footer,
    }
    
    return render(request, 'landing/index.html', contextvar)


def pricing_view(request):

    contextvar = {
        'customers': customers,
        'testimonials': testimonials,
        'testimonial_intro': testimonial_intro,
        'price_plans':price_plans,
        'navigation_links': navigation_links,
        'navigation_footer': navigation_footer,
    }

    return render(request, 'pricing/pricing.html', contextvar)


def about_view(request):

    about = About.objects.all().first()

    contextvar = {
        'services':services,
        'customers': customers,
        'customer_intro': customer_intro,
        'team_mates':team_mates,
        'team_mates_intro': team_mates_intro,
        'navigation_links': navigation_links,
        'navigation_footer': navigation_footer,
        'about': about,
    }

    return render(request, 'about/about.html', contextvar)


def projects_view(request):

    contextvar = {
        'customers': customers,
        'customer_intro': customer_intro,
        'projects': projects,
        'projects_intro': projects_intro,
        'navigation_links': navigation_links,
        'navigation_footer': navigation_footer,
    }

    return render(request, 'projects/projects.html', contextvar)
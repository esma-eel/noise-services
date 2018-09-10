from django.shortcuts import render, get_object_or_404
from .models import TeamMate
from projects.models import (Project)
from landing.models import Navigation
# Create your views here.

# Create your views here.



navigation_links = Navigation.objects.filter(for_footer=False).all()
navigation_footer = Navigation.objects.filter(for_footer=True).all()


def teammate(request, team_mate_id):
    team_mate_detail = get_object_or_404(TeamMate, pk=team_mate_id)
    
    team_mate_projects = Project.objects.filter(team_mates__id=team_mate_id).all()
   
    contextvar = {
        'team_mate_detail': team_mate_detail,
        'navigation_links': navigation_links,
        'navigation_footer': navigation_footer,
        'team_mate_projects':team_mate_projects,
    }

    return render(request, 'teammate.html', contextvar)
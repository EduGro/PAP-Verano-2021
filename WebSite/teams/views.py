from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Team, Player, Position


class IndexView(generic.ListView):
    template_name = 'teams/index.html'
    context_object_name = 'latest_team_list'

    def get_queryset(self):
        """Return the first five teams."""
        return Team.objects.order_by('team_name')[:5]

class DetailView(generic.DetailView):
    model = Team
    template_name = 'teams/detail.html'
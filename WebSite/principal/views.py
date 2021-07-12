import datetime

from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from teams.models import Team
from tournament.models import Tournaments

class IndexView(generic.ListView):
    template_name = 'principal/index.html'
    context_object_name = 'index'

    def get_queryset(self):
        """Return the first five teams."""
        return Team.objects.order_by('team_name')[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'tournament_started': Tournaments.objects.filter(tournament_start_date__lte = datetime.date.today()).filter(tournament_end_date__gte = datetime.date.today())[:4],
            'tournament_open': Tournaments.objects.filter(tournament_start_date__gte = datetime.date.today() + datetime.timedelta(days=1)).order_by('tournament_start_date')[:4],
            'tournament_close': Tournaments.objects.filter(tournament_end_date__lt = datetime.date.today()).order_by('tournament_end_date')[:4],
            'more_context': Tournaments.objects.all(),
            'latest_team_list': Team.objects.order_by('team_name')[:4],
        })
        return context
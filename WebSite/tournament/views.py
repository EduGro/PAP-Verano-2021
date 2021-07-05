from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Tournaments, Teams_Tournaments

class IndexView(generic.ListView):
    template_name = 'tournament/index.html'
    context_object_name = 'latest_tournament_list'

    def get_queryset(self):
        """Return the closest five tournaments."""
        return Tournaments.objects
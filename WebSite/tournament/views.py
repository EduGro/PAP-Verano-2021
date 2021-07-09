import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Tournaments


class IndexView(generic.ListView):
    template_name = 'tournament/index.html'
    model = Tournaments
    context_object_name = 'tournaments'

    def get_queryset(self):
        """Return the last five published polls."""
        return Tournaments.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            'tournament_started': Tournaments.objects.filter(tournament_start_date__lte = datetime.date.today())[:9],
            'tournament_open': Tournaments.objects.filter(tournament_start_date__gte = datetime.date.today() + datetime.timedelta(days=1)).order_by('tournament_start_date')[:9],
            'tournament_close': Tournaments.objects.filter(tournament_end_date__lt = datetime.date.today()).order_by('tournament_end_date')[:9],
            'more_context': Tournaments.objects.all(),
        })
        return context
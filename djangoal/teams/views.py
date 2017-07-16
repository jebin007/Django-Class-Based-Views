from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from . import models


def team_list(request):
    teams = models.Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(models.Team, pk=pk)
    return render(request, 'teams/team_detail.html', {'team': team})

class TeamListView(ListView):
    context_object_name = "teams"
    model = models.Team

class TeamDeatilView(DetailView):
    model = models.Team

class TeamCreateView(CreateView):
    model = models.Team
    fields = ("name", "practice_location", "coach")

    def get_initial(self):                              #this function auto selects the logged in coach when creating teams.
        initial = super().get_initial()
        initial["coach"] = self.request.user.pk
        return initial


class TeamUpdateView(UpdateView):
    model = models.Team
    fields = ("name", "practice_location", "coach")

class TeamDeleteView(DeleteView):
    model = models.Team
    success_url = reverse_lazy("teams:list")

    def get_queryset(self):                             #this function makes sure the coach can only delete their team memeber and not others.
        if not self.request.user.is_superuser:
            return self.model.objects.filter(coach=self.request.user)
        return self.model.objects.all()



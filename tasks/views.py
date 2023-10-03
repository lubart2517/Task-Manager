from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TaskType, Position, Worker, Team, Project, Task
# from .forms import (
#     DriverCreationForm,
#     DriverLicenseUpdateForm,
#     CarForm,
#     CarModelSearchForm,
#     ManufacturerNameSearchForm,
#     DriverUsernameSearchForm
# )


@login_required
def index(request):
    """View function for the home page of the site."""

    projects = Project.objects
    teams = Team.objects

    context = {
        "projects": projects,
        "teams": teams,
    }

    return render(request, "tasks/index.html", context=context)


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    queryset = Project.objects.prefetch_related("team__workers")


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse_lazy("tasks:project-detail", args=[self.object.pk])


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("tasks:index")


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    success_url = reverse_lazy("tasks:index")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team

    def get_success_url(self) -> str:
        return reverse_lazy("tasks:team-detail", args=[self.object.pk])


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("tasks:index")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    # form_class = WorkerCreationForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker

    def get_success_url(self) -> str:
        return reverse_lazy("tasks:worker-detail", args=[self.object.pk])


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("tasks:index")

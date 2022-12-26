from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView, ListView, DetailView, UpdateView, DeleteView, View
from . import models, forms
from users import mixins as user_mixins


class WorkspacesView(user_mixins.LoggedInOnlyView, ListView):

    """ HomeView Definition """

    template_name = "workspace/index.html"
    context_object_name = "workspaces"
    
    def get_queryset(self):
        filter_args = {}
        return models.Workspace.objects.filter(**filter_args).order_by("-created")
    

class SearchView(user_mixins.LoggedInOnlyView, View):

    """ SearchView Definition """

    def get(self, request):

        form = forms.SearchForm(request.GET)

        if form.is_valid():

            name = form.cleaned_data.get("name")
            host_institution = form.cleaned_data.get("host_institution")
            status = form.cleaned_data.get("status")

            filter_args = {}

            if host_institution is not None:
                filter_args["name"] = name

            if host_institution is not None:
                filter_args["host_institution"] = host_institution

            if status is not None:
                filter_args["status"] = status
                
            workspaces = models.Workspace.objects.filter(**filter_args).order_by("-created")

            return render(
                request, "workspace/index.html", {"form": form, "workspaces": workspaces}
            )

        else:
            form = forms.SearchForm()

        return render(request, "workspace/index.html", {"form": form})
    

class CreateWorkspaceView(user_mixins.LoggedInOnlyView, View):
    
    """ Workspace Create View Definition """

    def get(self, request):
        
        form = forms.WorkspaceForm()
        return render(request, "common/form.html", {"form": form})

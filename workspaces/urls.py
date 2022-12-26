from django.urls import path
from . import views

app_name = "workspaces"

urlpatterns = [
    # path("", views.ProjectsView.as_view(), name="search"),
    path("create/", views.WorkspacesView.as_view(), name="create"),
    # path("<int:pk>/", views.ProjectDetailView.as_view(), name="detail"),
    # path("<int:pk>/edit/", views.EditProjectView.as_view(), name="edit"),
    # path("<int:pk>/delete/", views.DeleteProjectView.as_view(), name="delete"),
]

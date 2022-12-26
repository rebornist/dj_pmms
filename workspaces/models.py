from django.db import models
from django.urls import reverse
from core import models as core_models



class Workspace(core_models.TimeStampedModel):

    """ Workspace Model Definition """

    name = models.CharField(max_length=255)
    business_amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, default='')
    status = models.BooleanField(default=True)
    start_date = models.DateField(blank=True, default='')
    end_date = models.DateField(blank=True, default='')
    implementation_year = models.PositiveSmallIntegerField()
    host_company = models.CharField(max_length=50, blank=True, default='')
    general_manager = models.CharField(max_length=50, blank=True, default='')
    general_manager_phone = models.CharField(max_length=50, blank=True, default='')
    general_manager_email = models.CharField(max_length=150, blank=True, default='')
    host_institution = models.CharField(max_length=50, blank=True, default='')
    host_manager = models.CharField(max_length=50, blank=True, default='')
    host_manager_phone = models.CharField(max_length=50, blank=True, default='')
    host_manager_email = models.CharField(max_length=150, blank=True, default='')
    host_address = models.CharField(max_length=255, blank=True, default='')
    workflow_active = models.BooleanField(default=False)
    author = models.ForeignKey(
        "users.User", related_name="user_projects", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"pk": self.pk})

from datetime import datetime
from django import forms
from django.forms import widgets
from . import models
        
    
class WorkspaceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "name": "validation-required"})
        self.fields["business_amount"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})
        self.fields["status"].widget.attrs.update({"class": "form-control", "name": "validation-select"})
        self.fields["implementation_year"].widget.attrs.update({"class": "form-control"})
        self.fields["host_company"].widget.attrs.update({"class": "form-control"})
        self.fields["general_manager"].widget.attrs.update({"class": "form-control"})
        self.fields["general_manager_phone"].widget.attrs.update({"class": "form-control"})
        self.fields["general_manager_email"].widget.attrs.update({"class": "form-control"})
        self.fields["host_institution"].widget.attrs.update({"class": "form-control"})
        self.fields["host_manager"].widget.attrs.update({"class": "form-control"})
        self.fields["host_manager_phone"].widget.attrs.update({"class": "form-control"})
        self.fields["host_manager_email"].widget.attrs.update({"class": "form-control"})
        self.fields["host_address"].widget.attrs.update({"class": "form-control"})
        
    class Meta:
        model = models.Workspace
        fields = (
            "name",
            "business_amount",
            "description",
            "status",
            "start_date",
            "end_date",
            "implementation_year",
            "host_company",
            "general_manager",
            "general_manager_phone",
            "general_manager_email",
            "host_institution",
            "host_manager",
            "host_manager_phone",
            "host_manager_email",
            "host_address",
        )
        widgets = {
            "start_date": widgets.DateInput(attrs={"class": "form-control", "id": "start_date", "type": "date"}),
            "end_date": widgets.DateInput(attrs={"class": "form-control", "id": "end_date", "type": "date"}),
        }
        
    def save(self, *args, **kwargs):
        workspace = super().save(commit=False)
        return workspace
from django.contrib import admin
from . import models

@admin.register(models.Workspace)
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "business_amount",
                    "host_institution",
                    "description",
                    "status",
                )
            },
        ),
        ("Business Period", {"fields": ("implementation_year", "start_date", "end_date")}),
        ("Person Concerned", {"fields": ("general_manager", "general_manager_phone", "host_manager", "host_manager_phone", "host_address")}),
    )

    list_display = (
        "name",
        "business_amount",
        "description",
        "status",
        "implementation_year",
        "host_institution",
    )

    list_filter = (
        "status",
        "implementation_year",
        "host_institution",
    )

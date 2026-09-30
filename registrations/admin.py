from django.contrib import admin

# Register your models here.

from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "phone_number",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone_number",
    )

    ordering = ("-created_at",)
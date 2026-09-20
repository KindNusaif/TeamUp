from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "mode", "is_published")
    list_filter = ("mode", "is_published")
    search_fields = ("name",)

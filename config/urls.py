from django.contrib import admin
from django.urls import path
from core.views import home, events, event_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("events/", events, name="events"),
    path("events/<int:event_id>/", event_detail, name="event_detail"),
]
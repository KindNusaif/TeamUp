from django.contrib import admin
from django.urls import include, path

from core.views import event_detail, events, home


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("events/", events, name="events"),
    path("events/<int:event_id>/", event_detail, name="event_detail"),
    path("accounts/", include("accounts.urls")),
]
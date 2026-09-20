from django.shortcuts import get_object_or_404, render

from events.models import Event


def home(request):
    return render(request, "core/home.html")


def events(request):
    query = request.GET.get("q", "").strip()

    event_list = Event.objects.filter(is_published=True)

    if query:
        event_list = event_list.filter(name__icontains=query)

    return render(
        request,
        "core/events.html",
        {
            "events": event_list,
            "query": query,
        },
    )


def event_detail(request, event_id):
    event = get_object_or_404(
        Event,
        pk=event_id,
        is_published=True,
    )

    return render(
        request,
        "core/event_detail.html",
        {"event": event},
    )

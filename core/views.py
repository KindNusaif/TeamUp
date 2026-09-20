from django.http import Http404
from django.shortcuts import render


# Fictional data for learning. We'll use a database later.
SAMPLE_EVENTS = [
    {
        "id": 1,
        "name": "Campus Hackathon",
        "mode": "Online",
        "description": "Build a useful solution to a student problem.",
    },
    {
        "id": 2,
        "name": "Green Tech Buildathon",
        "mode": "In person",
        "description": "Create a technology idea for a greener campus.",
    },
]


def home(request):
    return render(request, "core/home.html")


def events(request):
    query = request.GET.get("q", "").strip()

    filtered_events = [
        event
        for event in SAMPLE_EVENTS
        if query.casefold() in event["name"].casefold()
    ]

    return render(
        request,
        "core/events.html",
        {"events": filtered_events, "query": query},
    )


def event_detail(request, event_id):
    for event in SAMPLE_EVENTS:
        if event["id"] == event_id:
            return render(
                request,
                "core/event_detail.html",
                {"event": event},
            )

    raise Http404("Event not found")
from django.db import models


class Event(models.Model):
    class Mode(models.TextChoices):
        ONLINE = "online", "Online"
        IN_PERSON = "in_person", "In person"

    name = models.CharField(max_length=200)
    description = models.TextField()
    mode = models.CharField(
        max_length=20,
        choices=Mode.choices,
        default=Mode.ONLINE,
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

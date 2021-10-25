import uuid
from django.db import models


class Mentorship(models.Model):
    uuid = models.UUIDField(
            unique=True,
            default=uuid.uuid4,
            editable=False,
            )
    title = models.CharField(max_length=120)
    message = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    background = models.TextField(max_length=512)
    expectation = models.TextField(max_length=512)
    status = models.CharField(max_length=20, default="pending")
    mentee_id = models.CharField(max_length=32)
    mentor_id = models.CharField(max_length=32)

    def __str__(self):
        return self.mentee_id


class MentorshipResponse(models.Model):
    uuid = models.UUIDField(
            unique=True,
            default=uuid.uuid4,
            editable=False,
            )
    mentee_id = models.CharField(max_length=32)
    mentorship = models.OneToOneField(to=Mentorship, on_delete=models.PROTECT)
    message = models.TextField(max_length=512)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    link = models.CharField(max_length=128)


    def __str__(self):
        return self.mentorship.mentor_id

from django.contrib import admin
from .models import Mentorship, MentorshipResponse


@admin.register(Mentorship)
class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'title', 'background', 'message', 'status']


@admin.register(MentorshipResponse)
class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['mentee_id',  'uuid', 'mentorship', 'message', 'date',]

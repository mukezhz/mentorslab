from django.contrib import admin
from .models import Mentorship, MentorshipResponse


@admin.register(Mentorship)
class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'background', 'message', 'status']

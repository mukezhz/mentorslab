from django.contrib import admin
from .models import Forum, Comment, Vote, CommentVote


@admin.register(Forum)
class ForumModelAdmin(admin.ModelAdmin):
    list_display = [
            'topic',
            'author',
            'created_date'
            ]


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'forum',
            'created_date',
            ]


@admin.register(Vote)
class VoteModelAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'forum',
            'voter',
            'number',
            ]


@admin.register(CommentVote)
class CommentVoteModelAdmin(admin.ModelAdmin):
    list_display = [
            'id',
            'voter',
            'number',
            'comment',
            ]

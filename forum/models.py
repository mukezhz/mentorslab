import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

USER = get_user_model()


class Forum(models.Model):
    uuid = models.UUIDField(
            unique=True,
            default=uuid.uuid4,
            editable=False,
            )
    topic = models.CharField(max_length=150)
    body = models.TextField()
    tags = ArrayField(models.CharField(max_length=15))
    created_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
            to=USER,
            on_delete=models.CASCADE,
            related_name="authors")

    def __str__(self):
        return f"Forum: {self.topic}"


class VoteOption(models.IntegerChoices):
    NORMAL = 0, 'Normal'
    UP = 1, 'Up'
    DOWN = -1, 'Down'


class Vote(models.Model):
    forum = models.ForeignKey(
            Forum,
            related_name="formvotes",
            on_delete=models.CASCADE)
    number = models.IntegerField(
            default=VoteOption.NORMAL,
            choices=VoteOption.choices)
    voter = models.OneToOneField(
            USER,
            on_delete=models.CASCADE,
            related_name="formvoters")

    def __str__(self):
        return f"Vote: {self.forum.topic} {self.number}"


class Comment(models.Model):
    forum = models.ForeignKey(
            Forum,
            related_name="formcomments",
            on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    commentor = models.ForeignKey(
            USER,
            on_delete=models.CASCADE,
            related_name="formcommentors")

    def __str__(self):
        return f"Comment: {self.forum.topic}"


class CommentVote(models.Model):
    comment = models.ForeignKey(
            Comment,
            related_name="formcommentvotes",
            on_delete=models.CASCADE)
    number = models.IntegerField(
            default=VoteOption.NORMAL,
            choices=VoteOption.choices)
    voter = models.OneToOneField(
            USER,
            on_delete=models.CASCADE,
            related_name="formcommentvoters")

    def __str__(self):
        return f"CommentVote: {self.comment.forum.topic} {self.number}"

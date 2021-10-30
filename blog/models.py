import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

USER = get_user_model()


class Blog(models.Model):
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
            related_name="blogauthors")

    def __str__(self):
        return f"Blog: {self.topic}"


class BlogComment(models.Model):
    blog = models.ForeignKey(
            Blog,
            related_name="blogcomments",
            on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    commentor = models.ForeignKey(
            USER,
            on_delete=models.CASCADE,
            related_name="blogcommentors")

    def __str__(self):
        return f"BlogComment: {self.blog.topic}"

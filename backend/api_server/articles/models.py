from django.db import models
from django.contrib.auth import get_user_model


class Article(models.Model):
    class Meta:
        db_table = 'article'

    class Status(models.TextChoices):
        DRAFT = 'draft', 'DRAFT'
        PUBLISH = 'publish', 'PUBLISH'

    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    content = models.TextField()
    cover_article_url = models.URLField(null=False, blank=False)
    tags = models.TextField(max_length=400, null=False, blank=False, default="all")

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    view_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    up_votes = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

from rest_framework import serializers


class ArticlesGetSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    title = serializers.CharField(max_length=250, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=500, allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)
    cover_article_url = serializers.URLField(allow_null=False, allow_blank=False)
    tags = serializers.CharField(max_length=400, allow_null=False, allow_blank=False)

    view_count = serializers.IntegerField(min_value=0)
    comments_count = serializers.IntegerField(min_value=0)
    up_votes = serializers.IntegerField(min_value=0)

    created = serializers.DateTimeField()
    author = serializers.CharField()


class ArticlePostSerializer(serializers.Serializer):
    STATUS_CHOICES = (
        ("draft", "DRAFT"),
        ('publish', 'PUBLISH')
    )

    title = serializers.CharField(max_length=250, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=500, allow_null=False, allow_blank=False)
    content = serializers.CharField(allow_null=False, allow_blank=False)
    cover_article_url = serializers.URLField(allow_null=False, allow_blank=False)
    tags = serializers.CharField(max_length=400, allow_null=False, allow_blank=False)
    status = serializers.ChoiceField(choices=STATUS_CHOICES, default='draft', allow_null=True)


class ArticlesCounterPostSerializer(serializers.Serializer):
    view_count = serializers.IntegerField(min_value=0)
    comments_count = serializers.IntegerField(min_value=0)
    up_votes = serializers.IntegerField(min_value=0)

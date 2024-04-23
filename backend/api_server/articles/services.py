from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from articles.models import Article
from articles.serializers import ArticlesGetSerializer, ArticlePostSerializer


def get_serializer(*args, **kwargs):
    return ArticlesGetSerializer(*args, **kwargs)


def post_article_serializer(*args, **kwargs):
    return ArticlePostSerializer(*args, **kwargs)


def get_articles(*args, **kwargs):
    return get_list_or_404(Article.objects.order_by('-created'), *args, **kwargs)


def get_article_id(*args, **kwargs):
    return get_list_or_404(Article, *args, **kwargs)


def get_article_by_id(*args, **kwargs):
    return get_object_or_404(Article, *args, **kwargs)


def get_articles_user(*args, **kwargs):
    return get_list_or_404(Article, *args, **kwargs)


def update_article_model(**kwargs):
    return Article.objects.filter(id=kwargs.pop('id')).update(**kwargs)


def delete_article_model(**kwargs):
    return Article.objects.filter(id=kwargs.pop('id')).delete()


def create_article_model(*args, **kwargs):
    user = get_object_or_404(get_user_model(), *args, id=kwargs.pop('author'))

    return Article.objects.get_or_create(author=user, **kwargs)

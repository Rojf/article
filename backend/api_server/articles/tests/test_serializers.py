import datetime

from django.test import TestCase
from articles.serializers import ArticlesGetSerializer, ArticlePostSerializer


data = {
    'id': 1,
    'title': 'Название статьи',
    'description': 'Описание статьи',
    'content': 'Содержание статьи',
    'cover_article_url': 'https://example.com/article',
    'tags': 'django, python, web-development',
    'view_count': 100,
    'comments_count': 5,
    'up_votes': 10,
    'author': 'user123',
    'created': datetime.datetime(2024, 4, 18, 10, 30, 0),
    'updated': datetime.datetime(2024, 4, 19, 15, 0, 0)
}

data_1 = {
    'id': 1,
    "title": "Название статьи",
    "description": "Описание статьи",
    "content": "Содержание статьи",
    "cover_article_url": "https://example.com/article",
    "tags": "django, python, web-development",
    "view_count": 100,
    "comments_count": 5,
    "up_votes": 10,
    "author": "user123",
    "created": "2024-04-18T10:30:00Z",
    "updated": "2024-04-19T15:00:00Z"
}

data_2 = {
    'id': 1,
    'title': 'Название статьи',
    'description': 'Описание статьи',
    'content': 'Содержание статьи',
    'cover_article_url': 'https://example.com/article',
    'tags': 'django, python, web-development',
    'view_count': 100,
    'comments_count': 5,
    'up_votes': 10,
    'author': 'user123',
    'created': datetime.datetime(2024, 4, 18, 10, 30, 0),
    'updated': datetime.datetime(2024, 4, 19, 15, 0, 0),
    'hello': 'hello',
}

data_3 = {
    'id': 1,
    'title': 'A' * 240,  # Длина больше максимальной
    'description': 'T' * 490,
    'tags': 't' * 390
}


class ArticlesGetSerializerTestCase(TestCase):

    def test_articles_serializer(self):
        serializer_1 = ArticlesGetSerializer(data=data_1)
        serializer_2 = ArticlesGetSerializer(data=data_2)

        self.assertTrue(serializer_1.is_valid())
        self.assertTrue(serializer_2.is_valid())

    def test_max_length(self):
        serializer = ArticlesGetSerializer(data=data_3)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].max_length, 250)
        self.assertEqual(serializer.fields['description'].max_length, 500)
        self.assertEqual(serializer.fields['tags'].max_length, 400)

    def test_allow_null(self):
        serializer = ArticlesGetSerializer(data=data)


        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].allow_null, False)
        self.assertEqual(serializer.fields['description'].allow_null, False)
        self.assertEqual(serializer.fields['content'].allow_null, False)
        self.assertEqual(serializer.fields['cover_article_url'].allow_null, False)
        self.assertEqual(serializer.fields['tags'].allow_null, False)

    def test_allow_blank(self):
        serializer = ArticlesGetSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].allow_blank, False)
        self.assertEqual(serializer.fields['description'].allow_blank, False)
        self.assertEqual(serializer.fields['content'].allow_blank, False)
        self.assertEqual(serializer.fields['cover_article_url'].allow_blank, False)
        self.assertEqual(serializer.fields['tags'].allow_blank, False)

    def test_date_field_label(self):
        serializer = ArticlesGetSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertTrue(serializer.fields['title'].label == 'Title')
        self.assertTrue(serializer.fields['description'].label == 'Description')
        self.assertTrue(serializer.fields['content'].label == 'Content')
        self.assertTrue(serializer.fields['cover_article_url'].label == 'Cover article url')
        self.assertTrue(serializer.fields['tags'].label == 'Tags')


class ArticlesPostSerializerTestCase(TestCase):

    def test_articles_serializer(self):
        serializer_1 = ArticlePostSerializer(data=data_1)
        serializer_2 = ArticlePostSerializer(data=data_2)

        self.assertTrue(serializer_1.is_valid())
        self.assertTrue(serializer_2.is_valid())

    def test_max_length(self):
        serializer = ArticlesGetSerializer(data=data_3)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].max_length, 250)
        self.assertEqual(serializer.fields['description'].max_length, 500)
        self.assertEqual(serializer.fields['tags'].max_length, 400)

    def test_allow_null(self):
        serializer = ArticlePostSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].allow_null, False)
        self.assertEqual(serializer.fields['description'].allow_null, False)
        self.assertEqual(serializer.fields['content'].allow_null, False)
        self.assertEqual(serializer.fields['cover_article_url'].allow_null, False)
        self.assertEqual(serializer.fields['tags'].allow_null, False)

    def test_allow_blank(self):
        serializer = ArticlePostSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.fields['title'].allow_blank, False)
        self.assertEqual(serializer.fields['description'].allow_blank, False)
        self.assertEqual(serializer.fields['content'].allow_blank, False)
        self.assertEqual(serializer.fields['cover_article_url'].allow_blank, False)
        self.assertEqual(serializer.fields['tags'].allow_blank, False)

    def test_date_field_label(self):
        serializer = ArticlePostSerializer(data=data)

        self.assertTrue(serializer.is_valid())
        self.assertTrue(serializer.fields['title'].label == 'Title')
        self.assertTrue(serializer.fields['description'].label == 'Description')
        self.assertTrue(serializer.fields['content'].label == 'Content')
        self.assertTrue(serializer.fields['cover_article_url'].label == 'Cover article url')
        self.assertTrue(serializer.fields['tags'].label == 'Tags')

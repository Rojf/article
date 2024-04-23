from django.test import TestCase
from articles.models import Article


title = 'Архитектура в Django проектах — как выжить',
description = 'Думаю, ни для кого не секрет, что в разговорах опытных разработчиков Python, и не только, часто ' \
               'проскальзывают фразы о том, что Django это зло, что в Django плохая архитектура и на ней невозможно ' \
               'написать большой проект без боли. Часто даже средний Django проект сложно поддерживать и расширять. ' \
               'Предлагаю разобраться, почему так происходит и что с Django проектами не так.'
content = 'Думаю, ни для кого не секрет, что в разговорах опытных разработчиков Python, и не только, часто ' \
           'проскальзывают фразы о том, что Django это зло, что в Django плохая архитектура и на ней невозможно ' \
           'написать большой проект без боли. Часто даже средний Django проект сложно поддерживать и расширять. ' \
           'Предлагаю разобраться, почему так происходит и что с Django проектами не так.'
cover_article_url = 'https://habrastorage.org/r/w780/getpro/habr/upload_files/c60/a75/0b3/c60a750b3f542e0110a9d4a' \
                     '176d09763.jpg'
tags = 'django,архитектура,python'


class ArticleTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title=title, description=description, content=content, cover_article_url=cover_article_url, tags=tags,
        )

    def test_title_is_true(self):
        article_1 = Article.objects.get(id=1)

        title_1 = article_1._meta.get_field('title').verbose_name

        self.assertEqual(title_1, 'title')

    def test_description_is_true(self):
        article_1 = Article.objects.get(id=1)

        title_1 = article_1._meta.get_field('description').verbose_name

        self.assertEqual(title_1, 'description')

    def test_content_is_true(self):
        article_1 = Article.objects.get(id=1)

        title_1 = article_1._meta.get_field('content').verbose_name

        self.assertEqual(title_1, 'content')

    def test_cover_article_url_is_true(self):
        article_1 = Article.objects.get(id=1)

        title_1 = article_1._meta.get_field('cover_article_url').verbose_name

        self.assertEqual(title_1, 'cover article url')

    def test_tags_is_true(self):
        article_1 = Article.objects.get(id=1)

        title_1 = article_1._meta.get_field('tags').verbose_name

        self.assertEqual(title_1, 'tags')

    def test_max_length(self):
        article_1 = Article.objects.get(id=1)

        max_length_title = article_1._meta.get_field('title').max_length
        max_length_description = article_1._meta.get_field('description').max_length
        max_length_tags = article_1._meta.get_field('tags').max_length

        self.assertEqual(max_length_title, 300)
        self.assertEqual(max_length_description, 500)
        self.assertEqual(max_length_tags, 400)

    def test_null(self):
        article_1 = Article.objects.get(id=1)

        null_title = article_1._meta.get_field('title').null
        null_description = article_1._meta.get_field('description').null
        null_content = article_1._meta.get_field('content').null
        null_cover_article_url = article_1._meta.get_field('cover_article_url').null
        null_tags = article_1._meta.get_field('tags').null

        self.assertEqual(null_title, False)
        self.assertEqual(null_description, False)
        self.assertEqual(null_content, False)
        self.assertEqual(null_cover_article_url, False)
        self.assertEqual(null_tags, False)

    def test_blank(self):
        article_1 = Article.objects.get(id=1)

        blank_title = article_1._meta.get_field('title').blank
        blank_description = article_1._meta.get_field('description').blank
        blank_content = article_1._meta.get_field('content').blank
        blank_cover_article_url = article_1._meta.get_field('cover_article_url').blank
        blank_tags = article_1._meta.get_field('tags').blank

        self.assertEqual(blank_title, False)
        self.assertEqual(blank_description, False)
        self.assertEqual(blank_content, False)
        self.assertEqual(blank_cover_article_url, False)
        self.assertEqual(blank_tags, False)

    def test_default(self):
        article_1 = Article.objects.get(id=1)

        default_tags = article_1._meta.get_field('tags').default

        self.assertEqual(default_tags, 'all')

    def test_object_name(self):
        article_1 = Article.objects.get(id=1)

        expected_object_title = article_1.title

        self.assertEqual(expected_object_title, str(article_1))

    def test_data_correctness(self):
        article_1 = Article.objects.get(id=1)

        expected_object_title_1 = article_1.title
        expected_object_description_1 = article_1.description
        expected_object_content_1 = article_1.content
        expected_object_cover_article_url_1 = article_1.cover_article_url
        expected_object_tags_1 = article_1.tags

        self.assertEqual(expected_object_title_1, str(article_1))
        self.assertTrue(expected_object_description_1, description)
        self.assertEqual(expected_object_content_1, content)
        self.assertEqual(expected_object_cover_article_url_1, cover_article_url)
        self.assertEqual(expected_object_tags_1, tags)

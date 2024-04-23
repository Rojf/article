from django.test import TestCase
import requests

class ArticleCurlGetTestCase(TestCase):
    def test_curl_get_api_v1_articles(self):
        url = 'http://127.0.0.1:8000/api/v1/articles'
        headers = {'Content-Type': 'application/json'}
        data = {
            'title': 'Test Article',
            'description': 'This is a test article',
            'content': 'Lorem ipsum dolor sit amet',
            'cover_article_url': 'https://example.com/image.jpg',
            'tags': 'test, article'
        }

        # Отправка POST-запроса с помощью requests
        response = requests.get(url, headers=headers, json=data)

        # Проверка статуса ответа
        self.assertEqual(response.status_code, 200)  # Предполагая, что статус 201 - Created

        # Проверка содержимого ответа
        article_data = response.json()
        print(article_data[0]['title'])
        self.assertEqual(article_data[0]['title'], 'Архитектура в Django проектах — как выжить')
        self.assertEqual(article_data[0]['description'], 'Думаю, ни для кого не секрет, что в разговорах '
                                                         'опытных разработчиков Python, и не только, часто '
                                                         'проскальзывают фразы о том, что Django это зло, что в Django '
                                                         'плохая архитектура и на ней невозможно написать большой '
                                                         'проект без боли. Часто даже средний Django проект сложно '
                                                         'поддерживать и расширять. Предлагаю разобраться, почему так '
                                                         'происходит и что с Django проектами не так.')
        self.assertEqual(article_data[0]['content'], 'Думаю, ни для кого не секрет, что в разговорах опытных '
                                                     'разработчиков Python, и не только, часто проскальзывают фразы о '
                                                     'том, что Django это зло, что в Django плохая архитектура и на '
                                                     'ней невозможно написать большой проект без боли. Часто даже '
                                                     'средний Django проект сложно поддерживать и расширять. Предлагаю '
                                                     'разобраться, почему так происходит и что с Django проектами не '
                                                     'так.')
        self.assertEqual(article_data[0]['cover_article_url'], 'https://habrastorage.org/r/w780/getpro/habr/uplo'
                                                               'ad_files/c60/a75/0b3/c60a750b3f542e0110a9d4a176d09763.'
                                                               'jpg')
        self.assertEqual(article_data[0]['tags'], 'django,архитектура,python')
        self.assertEqual(article_data[0]['view_count'], 0)
        self.assertEqual(article_data[0]['comments_count'], 0)
        self.assertEqual(article_data[0]['up_votes'], 0)
        self.assertEqual(article_data[0]['created'], '2024-04-19T03:04:42.547258Z')
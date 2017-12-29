import unittest
from fabulous.services import news
from fabulous.services.secret_example import NEWS_API
''' In python3 mock is part of unittest
for python2 we need to install mock seperately 
'''
try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch, MagicMock


SOURCEBASEURL = "https://newsapi.org/v1/sources?"
ARTICLEBASEURL = "https://newsapi.org/v1/articles?"
QUERY = ['news', 'us', 'gaming', 'en']

DUMMY_SOURCE_RESPONCE = {
    "status": "ok",
    "sources": [
        {
            "id": "abc-news-au",
            "name": "ABC News (AU)"
        }
    ]
}

class TestNewsAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('fabulous.services.news.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()


    def test_source_end_point_called_with_right_parameters(self):
        language = 'en'
        country = 'us'
        category = 'gaming'
        source_query = {
            'language':language,
            'country': country,
            'category':category
        }
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {}

        news.fetchNews(QUERY)

        self.assertTrue(self.mock_get.cal)
        self.mock_get.assert_called_with(news.sourceBaseURL, params=source_query)

    def test_source_end_point_called_when_no_parameters_are_passed(self):
        language = 'en'
        country = 'in'
        category = 'general'

        source_query = {
            'language':language,
            'country': country,
            'category':category
        }

        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {}

        news.fetchNews('news')

        self.assertTrue(self.mock_get.cal)
        self.mock_get.assert_called_with(news.sourceBaseURL, params=source_query)

    def test_error_msg_return_when_source_end_point_sends_an_error_responce(self):
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {'status':'error'}

        responce = news.fetchNews('news')

        self.assertEqual(responce, news.SOURCE_ERR)





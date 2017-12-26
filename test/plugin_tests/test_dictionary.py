import unittest
from fabulous.services import dictionary
''' In python3 mock is part of unittest
for python2 we need to install mcok seperately 
'''
try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch


''' Dummy responce from the urbandictionary API'''
dictionary_responce = { 
    "list": [
        {
            "defid": 708924,
            "word": "test",
            "author": "tester",
            "permalink": "http:\/\/test.urbanup.com\/708924",
            "definition": "A process for testing things",
            "example": "This is a test message",
            "thumbs_up": 376,
            "thumbs_down": 221,
            "current_vote": ""
        },
    ]
}


class TestDictionaryService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('fabulous.services.dictionary.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()

    def test_dict_returns_correct_word(self):
        ''' Calls the dict method with a word and tests
        if the word is present in the responce '''
        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = dictionary_responce

        query = 'test'
        responce = dictionary.dict(query)

        ''' Tests that the mocked get have been called'''
        self.assertTrue(self.mock_get.called)
        self.assertIn(query, responce)
    
    def test_dict_returns_example_and_defination_when_responce_is_not_None(self):
        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = dictionary_responce

        query = 'test'
        responce = dictionary.dict(query)

        self.assertTrue(self.mock_get.called)
        self.assertIn('A process for testing things', responce)
        self.assertIn('This is a test message', responce)

    def test_dict_returns_error_message_when_responce_is_None(self):
        ''' set the return value of requests.get.json to None '''
        self.mock_get.return_value.json.return_value = None

        query = 'test'
        responce = dictionary.dict(query)

        self.assertTrue(self.mock_get.called)
        self.assertEqual(dictionary.ERROR_MSG, responce)

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


class TestDictionarServices(unittest.TestCase):

    @patch('fabulous.services.dictionary.requests.get')
    def test_responce_is_not_none(self, mock_get):
        mock_get.return_value.ok = True
        query = 'Test'
        responce =  dictionary.dict(query)
        self.assertIsNotNone(responce)
    
    ''' Test the processing of responce from urbandictionary API'''
    @patch('fabulous.services.dictionary.requests.get')
    def test_getting_defination_when_responce_is_not_none(self, mock_get):
        ''' Configure the mock to return a responce with an OK status.
        Also configures a JSON Method that returns the dictionary of word definations'''
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = dictionary_responce

        query = 'test'
        responce = dictionary.dict(query)
        self.assertIn('This is a test message', responce)
        self.assertIn('A process for testing things',responce)

if __name__ == '__main__':
    unittest.main()

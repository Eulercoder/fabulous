import unittest
from fabulous.services import stackoverflow
from fabulous.services.stackoverflow import SOF_BASEURL
''' In python3 mock is part of unittest
for python2 we need to install mock seperately 
'''
try:
    from unittest.mock import Mock, patch
except ImportError:
    from mock import Mock, patch, MagicMock


QUERY = 'ImportError in python'
payload = {'order':'desc', 'sort':'relevance', 'q': QUERY, 'accepted':'True', 
           'site':'stackoverflow'}

DUMMY_STACKOVERFLOW_RESPONCE = {
    "items":[
        {
            "link":"https://stackoverflow.com/questions/338768/python-error-importerror-no-module-named"
        }
    ]
}

class TestStackOverFlowService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('fabulous.services.dictionary.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()

    def test_sof_called_api_endpoint_with_correct_parameters(self):
        ''' Mock Does not provide implementation for __getitem__ which is used in sof method'''
        self.mock_get.return_value = MagicMock()

        stackoverflow.sof(QUERY)

        self.assertTrue(self.mock_get.called)
        self.mock_get.assert_called_with(SOF_BASEURL, params=payload)

    def test_error_msg_return_when_responce_is_not_valid(self):
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {}

        responce = stackoverflow.sof(QUERY)
        
        self.assertTrue(self.mock_get.called)
        self.assertEqual(responce, stackoverflow.KEY_ERROR_MSG)

    def test_sof_handles_data_when_responce_is_valid(self):
        self.mock_get.return_value =  MagicMock()
        self.mock_get.return_value.json.return_value = DUMMY_STACKOVERFLOW_RESPONCE

        responce = stackoverflow.sof(QUERY)

        self.assertTrue(self.mock_get.called)
        self.assertEqual(responce, DUMMY_STACKOVERFLOW_RESPONCE["items"][0]["link"])

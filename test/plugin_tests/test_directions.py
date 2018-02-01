import unittest
from fabulous.services import directions
from fabulous.services.secret_example import GOOGLE_DIRECTION_API
from fabulous.services.directions import DIRECTIONS_BASEURL
''' In python3 mock is part of unittest
for python2 we need to install mcok seperately 
'''
try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch

ORIGIN = 'PLACE_A'
DESTINATION = 'PLACE_B'
payload = {'origin':ORIGIN, 'destination':DESTINATION}


DUMMY_RESPONCE = {'status': '',
                   'error_message':''}

class TestDirectionService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('fabulous.services.dictionary.requests.get')
        cls.mock_Client_patcher = patch("fabulous.services.directions.googlemaps.Client.__init__")
        cls.mock_get = cls.mock_get_patcher.start()
        cls.mock_Client = cls.mock_Client_patcher.start()
        cls.mock_Client.return_value = None

    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()
        cls.mock_Client_patcher.stop()

    def test_googlemaps_client_called_with_api_key(self):
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {}

        directions.directions(ORIGIN, DESTINATION)

        self.assertTrue(self.mock_Client.called)
        self.mock_Client.assert_called_with(GOOGLE_DIRECTION_API)

        self.assertTrue(self.mock_Client)
        self.mock_Client.assert_called_with(GOOGLE_DIRECTION_API)

    def test_directions_call_api_with_correct_parameter(self):
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = {}

        responce =  directions.directions(ORIGIN,DESTINATION)

        self.assertTrue(self.mock_get.called)
        self.mock_get.assert_called_with(DIRECTIONS_BASEURL, params=payload)

    def test_directions_return_error_msg_when_responce_status_is_not_ok(self):
        self.mock_get.return_value = MagicMock()
        self.mock_get.return_value.json.return_value = DUMMY_RESPONCE

        responce = directions.directions(ORIGIN,DESTINATION)

        self.assertTrue(self.mock_get.called)
        self.assertEqual(directions.ERROR_MSG, responce)

    

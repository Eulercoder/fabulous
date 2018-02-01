import unittest
from fabulous.services import finance
''' In python3 mock is part of unittest
for python2 we need to install mcok seperately '''
try:
    from unittest.mock import Mock, patch
except:
    ImportError
    from mock import Mock, patch
from fabulous.services.secret_example import ALPHA_VANTAGE_STOCK_API
from fabulous.services.finance import FINANCE_BASEURL

QUERY = 'MSFT'
payload = {'function':'TIME_SERIES_INTRADAY', 'symbol':QUERY, 'interval':'1min', 
        'apikey':ALPHA_VANTAGE_STOCK_API}


DUMMY_ALPHA_VANTAGE_API_RESPONCE = {
    "Meta Data": {
        "1. Information": "Intraday (15min) prices and volumes",
        "2. Symbol": "MSFT",
        "3. Last Refreshed": "2017-12-26 16:00:00",
        "4. Interval": "1min",
        "5. Output Size": "Full size",
        "6. Time Zone": "US/Eastern"
    },
    "Time Series (1min)": {
        "2017-12-26 16:00:00": {
            "1. open": "85.3400",
            "2. high": "85.4300",
            "3. low": "85.3200",
            "4. close": "85.4000",
            "5. volume": "2296932"
        }
    }
}



class TestFinanceService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch('fabulous.services.dictionary.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()
    
    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()

    
    def test_stock_called_the_api_with_right_parameters(self):
        ''' Call the mocked requests.get and test if it's
            called with the right parameters '''
        
        responce = finance.stock(QUERY)

        self.assertTrue(self.mock_get.called)
        self.mock_get.assert_called_with(FINANCE_BASEURL, params= payload)

    def test_stock_returns_error_message_with_when_responce_is_not_valid(self):
        self.mock_get.return_value = Mock()
        ''' Returns an empty responce '''
        self.mock_get.return_value.json.return_value = {}

        responce = finance.stock(QUERY)

        self.assertTrue(self.mock_get.called)
        self.assertEqual(responce, finance.ERROR_MSG)
    
    def test_stock_handles_data_when_responce_is_valid(self):
        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = DUMMY_ALPHA_VANTAGE_API_RESPONCE

        responce = finance.stock(QUERY)

        self.assertTrue(self.mock_get.called)

        last_refreshed = DUMMY_ALPHA_VANTAGE_API_RESPONCE["Meta Data"]["3. Last Refreshed"]
        open_price = DUMMY_ALPHA_VANTAGE_API_RESPONCE["Time Series (1min)"][last_refreshed]["1. open"]
        close_price = DUMMY_ALPHA_VANTAGE_API_RESPONCE["Time Series (1min)"][last_refreshed]["4. close"]

        self.assertIn(QUERY, responce)
        self.assertIn(last_refreshed,responce)
        self.assertIn(open_price,responce)
        self.assertIn(close_price, responce)

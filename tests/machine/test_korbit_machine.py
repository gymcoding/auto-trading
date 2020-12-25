import unittest
from autotrading.machine.korbit_machine import KorbitMachine
import inspect

class KorbitMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.korbit_machine = KorbitMachine()

    def tearDown(self):
        pass

    def test_set_token(self):
        print(inspect.stack()[0][3])
        # {
        # 'access_token': '2DSXIxA54w5NJVvYpVCvNtnBS67MhmeJJMtIwp9bG9ZIZ1oUJQFj0tbcDwooN',
        # 'expires_in': 3540,
        # 'scope': 'VIEW,TRADE,WITHDRAWAL',
        # 'refresh_token': 'g43JKR4VYdBTFNA94EkYzL6y2x0cVAffr9FQMmQDxnKFXHyEMBZRlD8oUywbk',
        # 'token_type': 'Bearer'
        # }
        expire, access_token, refresh_token = self.korbit_machine.set_token(grant_type='password')
        assert access_token
        print(f'Expire: {expire}, AccessToken: {access_token}, RefreshToken: {refresh_token}')

    def test_get_token(self):
        print(inspect.stack()[0][3])
        self.korbit_machine.set_token(grant_type='password')
        access_token = self.korbit_machine.get_token()
        assert access_token
        print(f'AccessToken: {access_token}')
    
    def test_get_ticker(self):
        print(inspect.stack()[0][3])
        ticker = self.korbit_machine.get_ticker('etc_krw')
        assert ticker
        print(ticker)
    
    def test_get_filled_orders(self):
        print(inspect.stack()[0][3])
        order_book = self.korbit_machine.get_filled_orders(currency_type='btc_krw')
        assert order_book
        print(order_book)

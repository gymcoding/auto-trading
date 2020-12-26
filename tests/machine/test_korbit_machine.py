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

    def test_get_wallet_status(self):
        print(inspect.stack()[0][3])
        wallet_status = self.korbit_machine.get_wallet_status()
        assert wallet_status
        print(wallet_status)

    def test_buy_order(self):
        print(inspect.stack()[0][3])
        buy_order = self.korbit_machine.buy_order(
            currency_type='etc_krw',
            price='5000',
            qty='1',
            order_type='limit',
        )
        assert buy_order
        print(buy_order)
    
    def test_get_nonce(self):
        print(inspect.stack()[0][3])
        nonce = self.korbit_machine.get_nonce()
        assert nonce
        print(nonce)

    def test_sell_order(self):
        print(inspect.stack()[0][3])
        sell_order = self.korbit_machine.sell_order(currency_type='etc_krw', price='40000', qty='1', order_type='limit')
        assert sell_order
        print(sell_order)

    def test_cancel_order(self):
        print(inspect.stack()[0][3])
        cancel_order = self.korbit_machine.cancel_order(currency_type='etc_krw', order_id='5064611')
        assert cancel_order
        print(cancel_order)

    def test_get_my_order_status(self):
        print(inspect.stack()[0][3])
        my_order = self.korbit_machine.get_my_order_status(currency_type='etc_krw', order_id='5064611')
        assert my_order
        print(my_order)
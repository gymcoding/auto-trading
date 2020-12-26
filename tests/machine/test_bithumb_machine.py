import unittest
from autotrading.machine.bithumb_machine import BithumbMachine
import inspect

class BithumbMachineTestCase(unittest.TestCase):

    def setUp(self):
        self.bithumb_machine = BithumbMachine()
        
    def test_get_ticker(self):
        print(inspect.stack()[0][3])
        ticker = self.bithumb_machine.get_ticker('ETC')
        assert ticker
        print(ticker)

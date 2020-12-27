import unittest
from autotrading.pusher.slack_pusher import PushSlack

class TestSlacker(unittest.TestCase):
    def setUp(self):
        self.pusher = PushSlack()

    def test_send_message(self):
        self.pusher.send_message('#test-alarm-bot', 'Hello World~!')

    def tearDown(self):
        pass
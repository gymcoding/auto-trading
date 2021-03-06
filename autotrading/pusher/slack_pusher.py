from slacker import Slacker
from autotrading.pusher.base_pusher import Pusher
import configparser

class PushSlack(Pusher):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        token = config['SLACK']['token']
        self.slack = Slacker(token)

    def send_message(self, thread='#test-alarm-bot', message=None):
        self.slack.chat.post_message(thread, message)

import requests
import time
import math
import configparser
import json
import base64
import hashlib

class BithumbMachine():

    BASE_API_URL = 'https://api.bithumb.com'
    TRADE_CURRENCY_TYPE = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'BCH', 'XMR', 'ZEC', 'QTUM', 'BTG', 'EOS']

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.CLIENT_ID = config['BITHUMB']['client_id']
        self.CLIENT_SECRET = config['BITHUMB']['client_secret']
        self.USERNAME = config['BITHUMB']['username']

    # 마지막 체결 정보 조회
    def get_ticker(self, currency_type=None):
        if currency_type is None:
            raise Exception('Need to currency type')
        if currency_type not in self.TRADE_CURRENCY_TYPE:
            raise Exception('Not support currency type') 
        time.sleep(1)
        ticker_api_path = '/public/ticker/{currency}'.format(currency=currency_type)
        url_path = self.BASE_API_URL + ticker_api_path
        response = requests.get(url_path)
        response_json = response.json()
        result={}
        result['timestamp'] = str(response_json['data'].get('date'))
        result['last'] = response_json['data'].get('closing_price')
        result['bid'] = response_json['data'].get('buy_price')
        result['ask'] = response_json['data'].get('sell_price')
        result['high'] = response_json['data'].get('max_price')
        result['low'] = response_json['data'].get('min_price')
        result['volume'] = response_json['data'].get('volume_1day')
        return result

import requests
import time
import math
import configparser
import json
import base64
import hashlib
import hmac
import urllib

class BithumbMachine():

    BASE_API_URL = 'https://api.bithumb.com'
    TRADE_CURRENCY_TYPE = ['BTC', 'ETH', 'DASH', 'LTC', 'ETC', 'XRP', 'BCH', 'XMR', 'ZEC', 'QTUM', 'BTG', 'EOS', 'ICX', 'VEN', 'TRX', 'ELF', 'MITH', 'MCO', 'OMG', 'KNC', 'GNT', 'HSR' ]
    

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

    # 매매 완료 정보 조회
    def get_filled_orders(self, currency_type=None):
        if currency_type is None:
            raise Exception('Need to currency_type')
        if currency_type not in self.TRADE_CURRENCY_TYPE:
            raise Exception('Not support currency type')
        time.sleep(1)
        params = {
            'offset': 0,
            'count': 100,
        }
        orders_api_path = f'/public/transaction_history/{currency_type}'
        url_path = f'{self.BASE_API_URL}{orders_api_path}'
        print('url_path: ', url_path)
        response = requests.get(url_path, params=params)
        result = response.json()
        return result

    # 사용자 지갑정보 조회
    def get_wallet_status(self, currency_type=None):
        if currency_type is None:
            raise Exception('Need to currency_type')
        if currency_type not in self.TRADE_CURRENCY_TYPE:
            raise Exception('Not support currency type') 
        time.sleep(1)
        endpoint = '/info/balance'
        url_path = f'{self.BASE_API_URL}{endpoint}'
        
        endpoint_item_array = {
            'endpoint' : endpoint,
            'currency' : currency_type 
        }
        
        uri_array = dict(endpoint_item_array) # Concatenate the two arrays.
        str_data = urllib.parse.urlencode(uri_array)
        nonce = self.get_nonce()
        data = endpoint + chr(0) + str_data + chr(0) + nonce
        utf8_data = data.encode('utf-8')
        
        key = self.CLIENT_SECRET
        utf8_key = key.encode('utf-8')
       
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Api-Key': self.CLIENT_ID,
            'Api-Sign': self.get_signature(utf8_data, bytes(utf8_key)),
            'Api-Nonce': nonce,
        }
        print('headers: ', headers)
        print('str_data: ', str_data)
        response = requests.post(url_path, headers=headers, data=str_data)
        result = response.json()
        return result['data'] 

    
    def microtime(self, get_as_float=False):
        if get_as_float:
            return time.time()
        else:
            return '%f %d' % math.modf(time.time())

    def usecTime(self):
        mt = self.microtime(False)
        mt_array = mt.split(' ')[:2]
        return mt_array[1] + mt_array[0][2:5]

    def get_nonce(self):
        return self.usecTime() # str(int(time.time()))
    
    def get_signature(self, encoded_payload, secret_key):
        signature = hmac.new(secret_key, encoded_payload, hashlib.sha512);
        api_sign = base64.b64encode(signature.hexdigest().encode('utf-8'))
        return api_sign

    # 사용자 주문 목록 조회
    def get_list_my_orders(self, currency_type=None):
        if currency_type is None:
            raise Exception('Need to currency_type')
        if currency_type not in self.TRADE_CURRENCY_TYPE:
            raise Exception('Not support currency type') 
        time.sleep(1)
        endpoint ='/info/orders'
        url_path = self.BASE_API_URL + endpoint
        
        endpoint_item_array = {
            'endpoint' : endpoint,
            'order_currency' : currency_type
        }
        
        uri_array = dict(endpoint_item_array) # Concatenate the two arrays.
        str_data = urllib.parse.urlencode(uri_array)
        nonce = self.get_nonce()
        data = endpoint + chr(0) + str_data + chr(0) + nonce
        utf8_data = data.encode('utf-8')
        
        key = self.CLIENT_SECRET
        utf8_key = key.encode('utf-8')
       
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Api-Key': self.CLIENT_ID,
            'Api-Sign': self.get_signature(utf8_data, bytes(utf8_key)),
            'Api-Nonce': nonce,
        }
        response = requests.post(url_path, headers=headers, data=str_data)
        result = response.json()
        return result.get('data')


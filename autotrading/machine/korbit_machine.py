import configparser
import requests

# API call rate limit
# 안정적인 Korbit API 서비스 제공을 위하여 짧은 시간 내에 limit call rate을 초과하는 일정 빈도 이상의 호출은 허용되지 않는다.
# Access token 발급 및 갱신은 60분에 60번 호출할 수 있고,
# Ticker 기능은 60초에 60번 호출할 수 있으며,
# 이를 제외한 다른 모든 기능은 종류에 상관없이 도합 1초 동안 12번 호출이 가능하다.
class KorbitMachine():
    # REAT API 기본 URL
    BASE_API_URL = 'https://api.korbit.co.kr'

    # 코빗 API에서 지원하는 화폐 종류
    TRADE_CURRENCY_TYPE = ['btc', 'bch', 'btg', 'eth', 'etc', 'xrp', 'krw']

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.CLIENT_ID = config['KORBIT']['client_id']
        self.CLIENT_SECRET = config['KORBIT']['client_secret']
        self.USERNAME = config['KORBIT']['username']
        self.PASWORD = config['KORBIT']['password']
        self.access_token = None
        self.refresh_token = None
        self.token_type = None
    
    def set_token(self, grant_type='password'):
        token_api_path = '/v1/oauth2/access_token'
        url_path = f'{self.BASE_API_URL}{token_api_path}'

        if grant_type == 'password':
            data = {
                'client_id': self.CLIENT_ID,
                'client_secret': self.CLIENT_SECRET,
                'username': self.USERNAME,
                'password': self.PASWORD,
                'grant_type': grant_type,
            }
            print('data: ', data)
        elif grant_type == 'refresh_token':
            data = {
                'client_id': self.CLIENT_ID,
                'client_secret': self.CLIENT_SECRET,
                'refresh_token': self.refresh_token,
                'grant_type': grant_type,
            }
        else:
            raise Exception('Unexpected grant_type')
        
        response = requests.post(url_path, data=data)
        result = response.json()
        self.access_token = result['access_token']
        self.token_type = result['token_type']
        self.refresh_token = result['refresh_token']
        self.expire = result['expires_in']
        return self.expire, self.access_token, self.refresh_token

    def get_token(self):
        if self.access_token is not None:
            return self.access_token
        else:
            raise Exception('Need to set_token')


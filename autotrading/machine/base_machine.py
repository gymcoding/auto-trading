from abc import ABC, abstractmethod

class Machine(ABC):
    # 체결정보를 구하는 메서드
    @abstractmethod
    def get_filled_orders(self):
        pass

    # 마지막 체결정보를 구하는 메서드
    @abstractmethod
    def get_ticker(self):
        pass

    # 사용자의 지갑정보를 조회하는 메서드
    @abstractmethod
    def get_wallet_status(self):
        pass

    # 액세스 토큰 정보를 구하는 메서드
    @abstractmethod
    def get_token(self):
        pass

    # 액세스 토큰 정보를 만드는 메서드
    @abstractmethod
    def set_token(self):
        pass

    # 현재 사용자 이름을 구하는 메서드
    @abstractmethod
    def get_username(self):
        pass

    # 매수주문을 실행하는 메서드
    @abstractmethod
    def buy_order(self):
        pass

    # 매도주문을 실행하는 메서드
    @abstractmethod
    def sell_order(self):
        pass

    # 취소주문을 실행하는 메서드
    @abstractmethod
    def cancel_order(self):
        pass

    # 사용자의 주문 상세 정보를 조회하는 메서드
    @abstractmethod
    def get_my_order_status(self):
        pass

    
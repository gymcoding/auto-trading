# AutoTrading
코딩을 모르는 분들을 위하여, 가상화폐라는 주제로 파이썬을 배우며 가상화폐 자동매매 프로그램을 만들어가는 강좌 입니다.
코드는 저자 박재현님의 [파이썬으로 만드는 암호화폐 자동 거래 시스템](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&orderClick=JAa&barcode=9791158391027) 도서를 스터디 하고 참고하여 작성하였습니다.


## Test
- 클래스 단위 테스트
```sh
venv/bin/python -m unittest tests.machine.test_korbit_machine
```

- 특정 함수 테스트
```sh
venv/bin/python -m unittest tests.machine.test_korbit_machine.KorbitMachineTestCase.test_get_ticker
```

## MongoDB 에러 처리
- [certificate verify failed: unable to get local issuer certificate 에러처리](https://www.dev2qa.com/how-to-fix-python-error-certificate-verify-failed-unable-to-get-local-issuer-certificate-in-mac-os/0)

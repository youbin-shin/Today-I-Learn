# 과거

### OS

OS 커널별로 나눠보면 

- 모노리식 커널
  - uinx : Max, hpux, aix, soralix => 보통 대형시스템에서 많이 사용
  - liunx : 데미안(ubuntu), 레드햇(redhat, 센토os, 페도라), opnesuse BSD
- 마이크로 커널
- 하이브리드 커널
  - Windows NT 

### DB

- RDBMS 

  장점 : 무결성, 정규화 / 단점 : 정규화 필요

  - oracle : 공공기간이나 대형시스템에서 많이 사용
  - MySQL, Mariadb
  - MSSQL

- noSql 

  빅데이터에서 주로 사용

  - Key-value type DB
  - Document type DB (Monggo DB)
  - searchengin type DB (엘라스틱 서치)





## WAS

- container 를 코어로 가지고 있다. 

## Web Server

- 그림, 텍스트 등을 읽어 해석한 후 제공
- 종류
  - 바이너리 파일 제공
    - Nginx
    - Apache http
  - 소스 제공
    - django (python)
    - Node.js (javascript)

인터프리터 언어

- Web Server + container => tomcat, IIS `실행시켜줌`
- Web Server + container + J2EE 스펫 => `Was` Web logic, Jeus, jbos





---

백본

스위치

five wall

router

브라우저의 역할 : 보낸 요청을 텍스트로 받아 웹언어로 해석!

- 웹언어 : html, css, javascript, ...
  - react, angle, vue
- 인터넷
  - ISP
  - SKB, kT, LG U + , DNS
  - IP를 라우터에 보낸다!

----

# 현재

## HW

하드웨어 부분 : 백본, 스위치, five wall, router 전부 클라우드로 변함!!

- 클라우드 : AWS, MS-Azure, ....



IDC

I 전기 : 한국전력

​	ups가 있기에 한국전력이 끊겨도 보호된다!


## SW

OS, WAS 사이에 Docker가 생긴다!!

- docker : 반가상화
- Was라는 개념이 점점 사라짐
  - 핵심인 컨테이너만 남음
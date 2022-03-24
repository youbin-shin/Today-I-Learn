# 배포란 무엇인가 (Real artists ship)

2020.05.13

- Python anywhere 챗봇만들때 작성한 코드 했었다!!

- 배포라는 행위가 중요하다. 

#### Software Deplyment - 소프트웨어 배치

소프트웨어를 사용할 수 있도록 하는 모든 활동

##### Deployment is ?

- what : 우리는 서버컴퓨터에서 요청과 응답을 처리할 **프로그램**을 개발한다.
- when 
  - `개발`(Development stage) ->  `제품 출시 및 운영` (Production stage) 
    - `개발` : 개발 + 테스트 (TDD, Test Driven Development 작성후 개발하면서 진행, 테스트를 먼저하고 프로그램을 진행하기도 한다. 참고)
    - `제품 출시 및 운영` : **배포** + 운영
    - 배포를 기준으로 진행됐는지안됐는지 출시의 차이가 된다!
  - 위 과정을 계속 반복하기
- who, where
  - 제공자가 사용자 컴퓨터 ~~> 사용자가 사용자 컴퓨터에(cd, 디스켓으로) ~~> `Web App` 제공자가 제공자 컴퓨터에 + `Native App` 사용자가 사용자 컴퓨터에
  - Web App 제공자가??제공자의 컴퓨터에
- why
  - To us
  - Real Artists Ship
  - 완성은 시작보다 어려운 일이며 공개는 겁나는 일이다.

### 가상환경

1. #### 가상환경 생성 & 가상환경 활성화

   ```bash
   $ python -m venv (이름 설정)
   # 예시
   $ python -m venv myvenv # 현재 : 글로벌 -> 활성화 전이기때문
   
   $ souce myvenv/bin/activate # 활성화 시키는 코드
   (myvenv) $ pip list # 활성화 확인하기 위한 코드
   ```

   https://docs.python.org/ko/3/tutorial/venv.html

   - 활성화된 이후에는 django admin 명령어 사용 안된다!!

2. #### 장고 설치

3. #### `.gitignore` 설정

   `.gitignore.io` 사이트를 이용하여 추가가능

   또한 여기에 venv 관련된 것들도 있다.

   git init전에 가상환경안에 gitignore 넣어주자 => add 이후에 gitginore하지말기!!

4. #### git init

   ...

5. #### 의존성 파일 만들기 : requirements.txt

   주의 가상환경폴더를 깃헙을 올리지말기 -> 의존성파일로 올리기

   => 이를 통해 페어하고 있는 상대방과의 환경 동일하게 진행할 수 있도록!!

   계속 업데이트 가능

   ```bash
   # 의존성 관련 파일 올리기 위해서 다음 코드입력하기
   pip freeze > requirements.txt
   pip install -r requirements.txt
   ```

   




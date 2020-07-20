# 개발자가 되기 위한 준비

2020.01.20 ~ 2020.01.23

### git

- git bash 설치_리눅스 기반이기에

#### 설치방법

1. google에 git bash 검색 후 gitforwindows에서 다운로드하기

2. 계속 next하고  설치하기

   앞으로의 cmd 창

3. git bash 클릭하면 끝

#### cli 환경

- **pwd **: working directory 의 경로

- ~ 은 홈의 기호

  - 터미널은 항상 홈에서 켜진다
  - 홈의 위치 항상 중요(ex. c드라이브>사용자>multicampus)

- **ls** : working directory의 파일을 모두 볼 수 있음.

- **clear** : 목록을 정리하고 싶을 때 ( ctrl+L )

- **touch + (파일명)** : 파일 만들기 

- **mkdir + (폴더명)** : 폴더 만들기, make a directory 약자

- **rm + (파일명)** : 파일 지우기

- **rm + -r + (폴더명)** : 폴더 지우기

- **cd /** : 시스템의 최하단으로 이동

- **cd ~** : 홈 디렉토리로 이동

- **cd (이동하고 싶은 위치)/** : 작업할 공간 이동하기

- **cd ..** : 상위 폴더로 가기, 뒤로가기 버튼과 같은 기능

- **cd -** : 바로 직전의 곳으로 가기

#### git에 사용자 정보 입력하기

1. git config --global user. name {사용자 이름}

2. git config --global user.email {사용자 이메일}

3. git config --global --list

   입력시 입력한 정보 볼 수 있음.

#### git 단축키 만들기

1. git 화면에서 `code ~/.bashrc` 엔터

2. 새로열린 창에 단축키의 의미를 가진 `alias`을 이용한다.

   1. `alias (단축키)="(원래 작성해야하는 명령어)"`  작성한 뒤 저장한다.

      - 공백있으면 안된다.

      ex) `alias jp="jupyter notebook"`

   2. 리부팅을 해줘야하는 데 이때 git 에 `source ~/.bashrc`를 작성해주면 된다.

#### git 실습

- git 폴더를 만든 후 git 안에만 git init 설정하기

  관리할 폴더 최상단에만 한번 git init 해야해!!!!!

  만약 잘못 git init을 했으면 파일 보기에 숨긴 파일을 눌러 찾은 뒤에 삭제하면 된다.

- .git/ : 안보임

- git status : 가장 중요!! 상태 확인 가능

- git add (ex. a.py) : 추가 가능
  
  - git add . : 현재 위치에 있는 모든 파일을 한번에 다 올리기
  
- git status : 상태 확인

- git log : git의 기록, 가장 위에 있는 것이 최근 commit

- git commit -m "first commit" : commit 하기 ""안에 내용에 이름 넣어주면 된다.

- push
  - gitignore : gitHub에 올릴 경우 주요 개인정보와 같은 올리고 싶지 않은 파일 관리가능
  - 방법 : touch .gitignore > code .gitignore >
  
- : 보이면 q를 누르면 된다.

- git re~

#### git 순서 정리 (중간중간 git status 하기)

1. git init

2. git add .

3. git commit -m "commit message"

4. git remote add orfin <해당 git url>

5. git remote -v : remote 된 주소 확인

6. git push -u origin master

   - 반드시 commit 이후에 매번 push 할 필요없다.

   - add, commit은 세트~~!!

   - `git push -u origin master`이후에 push 명령어는 그냥` git push `라고만 해도 된다.

     단, -u를 빼서 사용하면  `git push origin master`이렇게 계속 같은 명령어를 사용해야한다.

   집에서 할 때는 github들어가서 clone하면 되는데 이미 init과 remote는 되어있기에 할 필요없다.

- git 주고받는 사이클
  - clone : 명령어 git clone 주소
  - push
  - pull : 명령어 git pull
    - clone과 pull의 차이 : 처음 설치할 때만 clone 이후에는 업데이트와 같은 기능이 pull이다!!!

#### gitignore

- project 에서 `git init` 한 후에 `touch.gitignore` 명령어로 만들면 된다.

- https://www.gitignore.io/

  - 위의 사이트에서 프로그램/언어(ex. django)를 입력하여 검색하면 찾을 수 있다.

    ![gitignore](https://user-images.githubusercontent.com/60081201/78453288-a5c7e100-76cb-11ea-8c90-f3aabe84b2c5.JPG)

- https://github.com/github/gitignore

  - 언어는 gitignore에서 퀼리티가 낮아서 `github.gitignore` 에서 추가하는 것이 좋다.

### GitHub


#### github에 이미지 올리는 방법

issues에 들어가서 write에 그림을 갖고 드래그하면 인터넷 주소가 된다.

이 주소를 md에 넣으면 된다. 

#### octotree

chrome 확장 프로그램 추가시 github 목록 보기 편하다.

---

### slack

- 개발자들의 카카오톡

- 다운로드 : slack 사이트 밑부분에 다운 64bit로



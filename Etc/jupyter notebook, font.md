2020.01.21

## jupyter notebook

git bash에 들어가서 `pip install notebook` 입력하여 설치한다.

`jupyter notebook`을 입력하면 볼 수 있다.



`h`를 누르면 명령어 확인 가능 

1. edit mode (초록)

   - ctrl + enter : 실행

   - shinft + enter : 셀이 없다면 만들고 있다면 이동

   - alt +enter : 셀 무조건 추가

   - esc를 누르면 command mode로

   - 모든 셀은 다 관여된다.

   - 별표가 되면 멈춘 것이기에 무한루프.. 

     해결방법 : kernel > restart&clear output 하면 된다.

2. command mode (파랑) 

   - d를 더블클릭하면 없어진다.
   - enter을 누르면 edit mode로
   - m을 누르면 markdown
   - a, b로 셀추가 a는 셀이 밑으로 b는 셀이 위로 생성



### jupyter notebook extension 설치하는 방법

**(번호 매겨주는 방법, 보기편한 방법)**

git rush에 

1. ```
   pip install jupyter_contrib_nbextensions
   ```

2. ```
   jupyter contrib nbextension install --user
   ```

 두개 설치하면 된다. 

이후 `jupyter notebook`을 하여 켜준다. 이후 Nbextensions에서 content를 찾아서 disable 앞에 체크박스를 지워주고 table of contents 체크를 해준뒤 다시 disable 앞에 체크박스로 잠궈주면 된다. 

### jupyter notebook 들어가는 방법

열고자하는 문서 빈곳에서 git bash를 열고 `jupyter notebook`입력하여 들어가기

---

## 프로그래밍 폰트 필요조건

1. 고정폭

   폰트가 차지하는 크기가 모두 동일

2. Sans-serif체
3. 가독성과 명확한 구분



### 폰트 종류

- hack font : 다운로드 hackfontsWindowsinstaller.exe 클릭
- souce code pro
- fira code
- jetbrains mono



### 폰트 바꾸기

1. 다운로드 이후 크롬 설정으로 들어가서 글꼴을 검색 > 글꼴 맞춤설정 > 고정폭 글꼴 >  hack

2. vsc에서는 톱니 모양의 버튼을 눌러서 Font Family에  앞 부분에 Hack,  추가해주면 된다.
3. git bash 에서 마우스 오른쪽 눌러서 options > text > select > hack으로 확인
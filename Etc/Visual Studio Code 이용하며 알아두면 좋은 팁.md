# Visual Studio Code 이용하며 알아두면 좋은 팁

## Visual Studio Code 코드 실행 방법 정리

### python

```bash
# 실행시킬 파일(ex 파일명 test.py) 위치에서
$ python test.py
```



### javascript

```bash
# 실행시킬 파일(ex 파일명 test.js) 위치에서
$ node test.js
```



## Visual Studio Code Extensions 정리

> Visual Studio Code 에서 유용한 extensions와 기능을 정리한다.

#### prettier :star:

- 저장 시에 코드 들여쓰기에 대한 컨벤션을 자동으로 맞춰준다. `opinionated code formatter`
- 설치 후 사용하는 방법
  1. ctrl + `,` 를 눌러 settings를 키고 Settings 글씨 옆에 파일 표시를 클릭하여 settings.json 파일을 연다.
  2. "editor.formatOnSave": true,
       "editor.formatOnType": true

#### Material Icon Theme

Material Design icons 들을 통해 파일에 대한 시각적인 구분을 높인다.

### HTML에서 유용한 extensions

#### Auto Close Tag

태그를 생성할 때 자동으로 닫는 태그가 생성된다.

#### Auto Rename Tag

태그를 변경할 경우 닫는 태그 또한 자동으로 변경된다.

#### live server 

자동으로 새로고침해준다.

#### HTML Snippets

괄호없는 태그이름을 입력하고 tab을 할 경우 태그가 형성된다.

### Vue에서 유용한 extensions

#### vue2snippets

저장시 자동으로 컨벤션을 지켜준다.

#### Bracket Pair Colorizer 2

괄호 매칭을 색을 통해 구분을 잘할 수 있도록 되도록 만들어준다.
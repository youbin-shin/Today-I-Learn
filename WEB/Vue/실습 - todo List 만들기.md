# 실습 - todo List 만들기

2020.05.26

### 1. 기본 준비

- vue.js cdn 추가한다.
- `div`에 id를 app으로 설정한 뒤 `script`에서 vue 설정한다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>todoList</title>
</head>
<body>
  <div id="app">
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
      const app = new Vue({
          el: '#app',
      });
  </script>   
</body>
</html>
```

### 2. todo List 항목 구현하기

- `script`에서 data에 todos를 리스트로 만든다.

  - 문제점 : 완료된 상태를 알 수 없다!
  - 해결 방법 : object로 표현하여 완료 항목을 추가한다.

  ```html
  <!-- todo에 대해 완료한 것을 구분할 수 없는 코드 -->
  <body>
    <div id="app">
      <ul>
        <li v-for="todo in todos">
          {{ todo }}
        </li>
      </ul>
   </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          todos: [
          'django 복습',
          '알고리즘 공부',
          'vuejs 복습',
          ]
        },
      });
    </script>
  </body>
  ```

- data 형태를 바꿔주고 `li` 태그에 v-for, v-if를 이용하여 구분하도록 한다.

  ```html
  <body>
    <div id="app">
      <ul>
        <li v-for="todo in todos" v-if="!todo.completed">
        <!-- false가 출력되기 위해 v-if에서 ! 이용하기 -->
          {{ todo.content }}
        </li>
        <li v-else>{{ todo.content }} [완료!]</li>
      </ul>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          todos: [
            {
              content: 'django 복습',
              completed: true
            },
            {
              content: '알고리즘 공부',
              completed: false
            },
            {
              content: 'vuejs 복습',
              completed: false
            },
          ]
        },
      });
    </script>
  </body>
  </html>
  ```

#### `v-for` 와 `v-if`

> - vue.js 가이드
>
>   [https://kr.vuejs.org/v2/guide/list.html#v-for-%EC%99%80-v-if](https://kr.vuejs.org/v2/guide/list.html#v-for-와-v-if)
>
>   동일한 노드에 두가지 모두 있다면 `v-for` 가 `v-if` 보다 높은 우선순위를 갖는다.

- for문이 돌 때마다 if문이 실행된다.

> - vue Style Guide
>
>   https://kr.vuejs.org/v2/style-guide/#sidebar-sponsors-special
>
>   vue 스타일 가이드/v-if와 v-for를 동시에 사용하지 마세요.

- `v-if`와 `v-for` 동시에 절대 사용하지 않는다.

- 사용 가능한 두가지 경우
  1. 리스트 목록을 필터링 하기 위한 경우
  2. 숨기기 위해 리스트의 랜더링을 피할 경우
- 해결 방법 (2가지)
  1. users을 새로운 computed 속성으로 필더링된 목록으로 대체한다.
  2. `v-if`를 컨테이너 엘리먼트로 옮겨준다.

### 3. todo 항목을 누르면 완료 표시가 뜨도록 하기

- methods를 통해 check 함수를 만든다.

  `todo.completed = !todo.completed` : 이를 통해 완료를 누르면 없어지도록(취소 가능하도록) 변경 가능하다.

- `li` 태그 안에 `v-on:click="check(todo)"` 를 넣어줌으로써 클릭했을 때마다 check 함수가 동작하도록 한다.

```html
<body>
  <div id="app">
    <ul>
      <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
        {{ todo.content }}
      </li>
      <li v-else v-on:click="check(todo)">{{ todo.content }} [완료!]</li>
    </ul>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        todos: [
          {
            content: 'django 복습',
            completed: true
          },
          {
            content: '알고리즘 공부',
            completed: false
          },
          {
            content: 'vuejs 복습',
            completed: false
          },
        ]
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed
        },
      }
    });
  </script>
</body>
</html>
```

### 4. 새로운 항목 추가 기능 만들기

todo list 작성할 수 있도록 하기 위해서는 **양방향 바인딩** `v-model`을 이용하면 된다.

- methods에 addTodo 함수를 만든다.

  todo 리스트에 추가되도록 `push`를 이용하고 리스트는 object 형태로 추가되어야 하기에 다음과 같이 `completed: false` 와 함께 추가한다.

- `input` 태그를 만들어 input에 입력되는 동시에 data에 들어갈 수 있도록 data에 `newTodo: '',`을 추가한다.

  양방향 바인딩을 위해 `input` 태그에  `v-model="newTodo"`를 추가한다.

- `button`을 통해 입력한 값이 추가되도록 `v-on:click="addTodo"`를 넣어준다.

  ---

- 추가) 항목이 추가된 후 입력 창을 초기화하기 위해 addTodo 함수 끝나기 전에 `this.newTodo = ''`를 추가한다.

```html
<body>
  <div id="app">
    <ul>
      <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
        {{ todo.content }}
      </li>
      <li v-else v-on:click="check(todo)">{{ todo.content }} [완료!]</li>
    </ul>
    <div>
      <input type="text" v-model="newTodo">
      <button v-on:click="addTodo">todo 추가하기</button>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        newTodo: '', // input에 입력되는 동시에 입력되도록!
        todos: [
          {
            content: 'django 복습',
            completed: true
          },
          {
            content: '알고리즘 공부',
            completed: false
          },
          {
            content: 'vuejs 복습',
            completed: false
          },
        ]
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed
        },
        addTodo: function () {
          this.todos.push({
            content: this.newTodo,
            completed:false
          })
          this.newTodo = '' // todo 추가 후 입력데이터 초기화
        },
      }
    });
  </script>
</body>
```

### 5. 완료된 할일 지우기

- methods에 clearCompleted 함수 만들기 이때 filter을 이용한다.

  - `.filter` : callback 함수의 return에 작성된 값으로 필터링된 결과(조건이 true인 것들)를 배열로 묶어서 반환한다.

    if 문 사용안하고 필터링으로 하면 된다.

  - if문 사용안하고 필터링으로 표현한다.

- `button` 에 `v-on:click="clearCompleted"` 로 양방향 바인딩하여 완료된 항목 지우도록 한다.

- 로직 정리
  1. todo.completed = true 인 항목을 제외시킨 나머지 (false) 들만 출력한다.
  2. 전체 todos 중에서 completed가 false인 것들만 모아서 새로운 todos를 만든다. => `.filter`

```html
<body>
  <div id="app">
    <ul>...
    </ul>
    <div>...
    </div>
        <button v-on:click="clearCompleted">완료된 할일 지우기</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {...
      methods: {
        check: function (todo) {...
        addTodo: function () {...
        clearCompleted: function () {
          const notCompletedTodos = this.todos.filter(todo => {
            // todo의 completed가 false인 object만 모아서 배열로 return
            return !todo.completed
          })
          this.todos = notCompletedTodos
        }
      }
    });
  </script>
</body>
```

#### 여기까지 구현한 총 코드

- 체크 박스 없다.
- 완료한 값에 취소선이 없다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>todo List</title>
</head>
<body>
  <div id="app">
    <ul>
      <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
      <!-- false가 출력되기 위해 v-if에서 ! 이용하기 -->
        {{ todo.content }}
      </li>
      <li v-else v-on:click="check(todo)">{{todo.content}} [완료!]</li>
    </ul>
    <!-- todo list 작성하기 ( 양방향 바인딩 => v-model )-->
    <div>
      <input type="text" v-model="newTodo">
      <button v-on:click="addTodo">todo 추가하기</button>
    </div>
    <button v-on:click="clearCompleted">완료된 할일 지우기</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        newTodo: '', 
        todos: [
          {
            content: 'django 복습',
            completed: true
          },
          {
            content: '알고리즘 공부',
            completed: false
          },
          {
            content: 'vuejs 복습',
            completed: false
          },
        ]
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed
        },
        addTodo: function () {
          this.todos.push({
            content: this.newTodo,
            completed:false
          })
          this.newTodo = '' // todo 추가 후 입력데이터 초기화
        },
        clearCompleted: function () {
          // filter : callback 함수의 return에 작성된 값으로 필터링된 결과를 배열로 묶어서 반환
          const notCompletedTodos = this.todos.filter(todo => {
            // todo의 completed가 false인 object만 모아서 배열로 return
            return !todo.completed
          })
          this.todos = notCompletedTodos
        }
      }
    });
  </script>
</body>
</html>
```

### 6. 체크 박스 만들기

- `input` 태그의 checkbox 타입을 이용하면서 `v-for`, `v-if` 를 같이 사용하는 것을 피할 수 있게 됐다.
- `v-model="todo.completed"` : todo.completed가 true면 해당 키 값이 활성화

```html
<body>
  <div id="app">
    <!--  -->
    <div v-for="todo in todos" >
      <input type="checkbox" v-model="todo.completed">
      <span>{{ todo.content }}</span>
      {{ todo.content }}
    </div>
```

> - vue.js 가이드
>
>   [https://kr.vuejs.org/v2/guide/list.html#%ED%95%84%ED%84%B0%EB%A7%81-%EC%A0%95%EB%A0%AC-%EB%90%9C-%EA%B2%B0%EA%B3%BC-%ED%91%9C%EC%8B%9C%ED%95%98%EA%B8%B0](https://kr.vuejs.org/v2/guide/list.html#필터링-정렬-된-결과-표시하기) 
>
>   vue.js/리스트 렌더링/필터링 정렬된 결과 표시하기

### 7. 취소선 만들기

- `style` 태그를 이용하여 취소선 만든다.

  class를 사용하여 `v-bind:class="{ completed: todo.completed }"` 를 통해 구현한다.

  (id는 javascript와 연결할 때 사용하도록 한다.)

```html
 <style>
    /* 취소선 */
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <div id="app">
    <div v-for="todo in todos" v-bind:class="{ completed: todo.completed }">
      <input type="checkbox" v-model="todo.completed">
      <span>{{ todo.content }}</span>
      {{ todo.content }}
    </div>
```

### 최종 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>todo List</title>
  <style>
    /* 취소선 */
    .completed {
      text-decoration: line-through;
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <div id="app">
    <!-- todo.completed가 true면 해당 키 값이 활성화 -->
    <div v-for="todo in todos" v-bind:class="{ completed: todo.completed }">
      <input type="checkbox" v-model="todo.completed">
      <span>{{ todo.content }}</span>
      {{ todo.content }}
    </div>

    <!-- todo list 작성하기 ( 양방향 바인딩 => v-model )-->
    <div>
      <input type="text" v-model="newTodo">
      <button v-on:click="addTodo">todo 추가하기</button>
    </div>
    <button v-on:click="clearCompleted">완료된 할일 지우기</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        newTodo: '', // input에 입력되는 동시에 입력되도록!
        todos: [
          {
            content: 'django 복습',
            completed: true
          },
          {
            content: '알고리즘 공부',
            completed: false
          },
          {
            content: 'vuejs 복습',
            completed: false
          },
        ]
      },
      methods: {
        check: function (todo) {
          todo.completed = !todo.completed
        },
        addTodo: function () {
          this.todos.push({
            content: this.newTodo,
            completed:false
          })
          this.newTodo = '' // todo 추가 후 입력데이터 초기화
        },
        clearCompleted: function () {
          // filter : callback 함수의 return에 작성된 값으로 필터링된 결과를 배열로 묶어서 반환
          const notCompletedTodos = this.todos.filter(todo => {
            // todo의 completed가 false인 object만 모아서 배열로 return
            return !todo.completed
          })
          this.todos = notCompletedTodos
        }
      }
    });
  </script>
</body>
</html>
```
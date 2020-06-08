# Vue 정리

2020.06.08

### Vue

프론트엔드 프레임워크 (Angular, React, Vue)

#### 왜 배우는 것인가?

데이터 변화하면 DOM을 변경하기 위해 배운다!

- data 변화 => DOM 변화 (data Vanila JS)
  - data, methods, computed, watched

  ---

- data
- methods : 데이터 조작
- computed : 데이터 조작 => 변수 (cache)

#### 컴포넌트로 (고도화) 관리 필요

- **Vue-SFC** 

  컴포넌트 간의 데이터 이동이 필요 => `단방향 흐름`으로 추적 용이하게

  - prop, emit

- 문제 발생 (불편)
  - 모든 컴포넌트에서 필요한 경우가 있음.
  - 비부모 자식간 데이터 이동도 필요함.

- 해결 방법
  - event bus
    - 데이터 추적 용이했던 단방향 패턴 불가해짐
  - **Vuex (Flux)**

#### Vuex

flux architecture

- props, emit을 기본적으로 하고 전체관리를 할 때는 Vuex 이용

  ---

- 데이터는 state에서 관리!

- 변경관리 : mutation/action

- getters




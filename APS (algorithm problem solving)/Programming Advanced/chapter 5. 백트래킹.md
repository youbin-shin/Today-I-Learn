

# chapter 5. 백트래킹

2020.05.15

### 백트래킹 (Backtracking) 개념

- 여러 가지 선택지 (옵션)들이 존재하는 상황에서 한가지를 선택한다.
- 선택이 이루어지면 새로운 선택지들의 집합이 생성된다.
- 이런 선택을 반복하면서 최종 상태에 도달한다.
  - 올바른 선택을 계속하면 목표 상태(goal state)에 도달한다.
  - 초기 상태(Root) => 경로탐색 => 목표 상태
- 당첨 리프노드 찾기
  1. 루프에서 갈 수 있는 노드를 선택한다.
  2. 꽝 노드까지 도달하면 최근의 선택으로 되돌아와서 다시 시작하낟.
  3. 더 이상의 선택지가 없다면 이전의 선택지로 돌아가서 다른 선택을 한다.
  4. 루트까지 돌아갔을 경우 더 이상 선택지가 없다면 찾는 답이 없다.
- `상태 공간 트리 (state space tree)` : 목표상태까지 가는 모든 경우의 수를 나타내는 트리
  - 루프 노드에서 리프(leaf)노드까지의 경로는 해답 후보 (candidate solution)라 한다. 

#### 백트래킹 vs 깊이 우선 탐색

- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 가지 않아 시도 횟수 줄임 (`Prunning` 가지치기)
  - 깊이 우선 탐색 : 모든 경로 추적 => 경우의 수 너무 많음
    - (N!가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색은 처리 불가능)
  - 백트래킹 : 불필요한 경로 조기에 차단
    - 일반적으로 경우의 수가 줄지만 최악의 경우에는 여전히 지수함수 시간 (Exponential Time)으로 처리 불가능

#### 백트래킹 기법

- 어떤 노드의 유망성을 점검한 후에 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
- 어떤 노드를 방문했을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
- 가지치기 (pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않는다.

#### 백트래킹을 이용한 알고리즘 절차

1. 상태 공간 트리의 깊이 우선 탐색을 실시
2. 각 노드가 유망한지 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 계속 검색

```python
def backtrack(선택 집합, 선택한수, 모든 선택수):
    if (선택한수==모든 선택수): # 더 이상 탐색할 노드가 없다.
        # 찾는 솔루션인지 체크
        return 결과
    # 현재 선택한 상태집합에 포함되지 않는 후보 선택들(노드) 생성 => 선택지 후보군 생성
    
    # 모든 후보 선택들에 대해
    {
        선택 집합에 하나의 후보 선택을 추가
        선택한 수 += 1
        결과 = backtrack 호출(선택집합, 선택한 수, 모든 선택수)
        
        if (결과 == 성공):
        	return 성공 # 성공한 경우 상위로 전달
    }
	return 실패
```

### 문제 제시 nQueen

- n X n 서양 장기판에서 배치한 Queen들이 서로 위협하지 않도록 n개의 Queen를 배치하는 문제이다. 어떤 두 Queen도 서로를 위협하지 않아야한다. Queen을 배치한 n 개의 위치는?

  ---

- 8 - Queens 문제
  - 후보해의 수 : 64C8 = 4426165368
  - 실제 해의 수 : 이중에서 실제 해는 92개 뿐
  - 최대한 효율적으로 찾아내는 것이 관건
- 4 - Queens 문제
  - 같은 행에 위치할 수 없다.
    - 모든 경우의 수 : 4 * 4 * 4 * 4 = 256

- 코드 구현

  ```python
  def backtrack(idx): # idx = 행
      global N, cnt
      # 최종상태인지 확인하고, 최종상태이면 해
      if idx == N:
          # 다 찾았음! 해
          cnt += 1
          return
      # 해당 상태에서 선택할 수 있는 후보군 생성
      # 노드가 유망한지 확인 : 열 + 상향 대각 + 하향 대각 => 유망한지
      for i in range(N):
          # if 열이 유망하고, 대각들이 유망
          if not col[i] and not dia_1[idx+i] and not dia_2[N+i-idx-1]:
              # 모든 후보군에 대해서 다음 상태 실행
              col[i] = 1
              dia_1[idx + i] = 1
              dia_2[N + i - idx - 1] = 1
              backtrack(idx + 1)
              col[i] = 0
              dia_1[idx + i] = 0
              dia_2[N + i - idx - 1] = 0            
  
  
  N = 4
  # 각 행에는 1개의 퀸만 올 수 있음
  col = [0] * N # 열의 사용여부를 판단하는 리스트
  dia_1 = [0] * (2 * N - 1) # 상향 대각 => r + c 번
  dia_2 = [0] * (2 * N - 1) # 하향 대각 => N + c - r + 1 번
  cnt = 0
  backtrack(0)
  print(cnt)
  ```

  - 상향 대각 : i와 j의 합이 같음
    - 개수 : N X 2 - 1
  - 하향 대각 : i - j의 차가 일정
    - 번째 대각선 : N - (i - j) - 1= N + j - i - 1 

### powerset 구하는 백트래킹 알고리즘

![image-20200515105016570](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200515105016570.png)

![image-20200515105106498](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200515105106498.png)

```python
def backtrack(selected, idx, input):
    # selected : 각 노드의 선택 여부를 판단하는 배열
    # idx : 깊이
    # input : 목표 개수
    candidates = [0] * 2 # 선택할 수 있는 선택지는 선택 o/x
    if idx == input:
        for i in range(input):
            if selected[i]:
                print(i, end=' ') # 배열인 경우 print(arr[i], end='')
        print()    
        return
	else:
        n_candidate = make_candidate(candidates) # 후보군 생성
        for i in range(n_candidate):
            selected[idx] = candidates[i]
            backtrack(selected, idx+1, input)
    
    
def make_candidate(candidates):
    candidates[0] = 1
    candidates[1] = 0
    return 2


N = 5
backtrack([0]*N, 0, N)

# 배열이면
arr = ['a'. 'b'. 'c', 'd']
```

```python
# 반복문 없이 구현

def backtrack(selected, idx, input):
    candidates = [0] * 2 # 선택할 수 있는 선택지는 선택 o/x
    if idx == input:
        for i in range(input):
            if selected[i]:
                print(i, end=' ') # 배열인 경우 print(arr[i], end='')
        print()    
        return
	else:
        selected[idx] = 1
        backtrack(selected, idx+1, input)
        selected[idx] = 0
        backtrack(selected, idx+1, input)           

N = 5
backtrack([0]*N, 0, N)
```

### 백트래킹을 이용하여 순열 구하기

```python
def backtrack(result, selected, idx, N):
    if idx == N:
        print(result)
        return
    # 사용가능한 선택지 후보군에 대하여 다음단계로 진행
    for i in range(N):
        if not selected[i]:
            selected[i] = 1
            result[idx] = i
            backtrack(result, selected, idx+1, N)
            selected[i] = 0
            
N = 5
backtrack([0]*N,[0]*N, 0, N)
```

![image-20200515124241334](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200515124241334.png)

### 연습문제 1

- {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.

- 코드 구현

  ```python
  def backtrack(arr, idx, N, selected, sum_num):
      if sum_num > 10:
          return
      if idx == N:
          # 총합이 10인 경우에만, 출력
          if sum_num == 10:
              for i in range(N):
                  if selected[i]:
                      print(arr[i], end=' ')
              print()
          return
      
      selected[idx] = 1
      backtrack(arr, idx+1, N, selected, sum_num+arr[idx])
      selected[idx] = 0   
      backtrack(arr, idx+1, N, selected, sum_num)
      
      
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  backtrack(arr, 0, 10, [0]*10, 0)
  ```




# 휴강 기간 알고리즘 e-learning 정리

> 3/2 월
>
> 1952 수영장
>
> 4008 숫자만들기



### 재귀함수 정리

- 호출 단계 n, 최종 단계 k 필요
- 다른 함수를 호출하는 과정과 같음!

```python
# 배열의 각 원소를 재귀함수로 접근하기

# n 현재 호출에서 접근할 원소의 인덱스
# k 배열의 크기

def f(n, k):
    if(n == k-1):
        print(A[n])
    else:
        f(n+1, k)
 
A = [1, 2, 3]
f(0, 3)
```

```python
# 재귀로 집합 A의 부분집합 만들기

def f(n, k):
    global b
    if n == k: # b의 모든 칸이 결정되는 경우
        for i in range(k):
            if b[i] == 1:
                print(b[i], end=' ')
        print()
        else:
            ...
        
    else:
        b[n] = 0
        f(n+1, k)
        b[n] = 1
        f(n+1, k)

A = [1, 2, 3]
b = [0] * len(A)
```

![image-20200306134723421](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200306134723421.png)

```python
# 부분집합 원소의 합

# 인덱스 n 이용
# n-1 번 원소까지 고려한 합 s
## n 번을 포함할 경우 s + A[n]
## n 번을 포함하지 않은 경우 s

def f(n, k, s):
    global maxV
    if n == k:
        if maxV < s:
            maxV = s
        ...        
    else:
        f(n+1, k, s+A[n])
        f(n+1, k, s)
```

```python
# 서로 다른 K 개의 자연수의 집합에서 부분집합 원소의 합이 M 인 경우의 수

def(n, k, s, M):
    global cnt
    if s == M:
        cnt += 1
        return
    elif n == k:
        return
    else:
        f(n+1, k, s+A[n], M)
        f(n+1, k, s, M)
```



### 1952. 수영장

n - 1월 까지의 비용 s

f(n, s)

```python
def f(n, s, d, m, m3):
    global minV
    if n > 12:
        if minV > s:
            minV = s 
    elif minV <= s: # 이미 최소비용이 넘어갔기에 제외시킴
        return
    else:
        f(n+1, s+min(table[n]*d,m), d, m, m3) # n월에 1일과 1달 비교한 이용권
        f(n+3, s+m3, d, m, m3) # n월에 3달 이용권

T = int(input())
for t in range(T):
    d, m, m3, y = map(int, input().split())
    table = [0] + list(map(int, input().split()))
    minV = y
    f(1, 0, d, m, m3)
    print('#{} {}'.format(t+1, minV))
```



### 4008. 숫자 만들기

- 음수에 대한 나눗셈 _ python 기준

  ```python
  a, b = -3, 2
  print(a//b) # -2
  print(int(a/b)) # -1, 현재 문제에서 사용할 경우
  if a < 0:
      print(-(abs(a)//b)) # -1
  else:
      print(a//b)
  ```

- 최대 최소 0으로 초기화하는 버릇 X

  문제에서 주어진 범위를 기준으로 초기화시켜주기

  ex) minV = 1000000, maxV = -10000000

```python
def f(n, k, r, op1, op2, op3, op4):
    global minV, maxV
    if n == k:
        if minV > r:
            r = minV
        if maxV < r:
            maxV = r
    else:
        if op1 > 0:
            f(n+1, k, r+card[n], op1-1, op2, op3, op4)
        if op2 > 0:
            f(n+1, k, r-card[n], op1, op2-1, op3, op4)
        if op3 > 0:
            f(n+1, k, r*card[n], op1, op2, op3-1, op4)
        if op4 > 0:
            f(n+1, k, int(r/card[n]), op1, op2, op3, op4-1)
```




# Programming Advanced

### 시작하기

#### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

- `int`, `format` 을 이용하여 문제 풀기

```python
for tc in range(int(input())):
    N, num = map(str, input().split())
    num_16 = int(num,16) # 16진수로 바꾸기
    num_2 = format(num_16,'b') # 2진수로 바꾸기
    while len(num_2) < int(N)*4: # 문제에 제시된 길이 맞춰주기
        num_2 = '0'+num_2
    print('#{} {}'.format(tc + 1, num_2))
```

- 아스키코드 이용하여 문제 풀기

```python
for tc in range(int(input())):
    N, num_16 = map(str, input().split())
    num_10 = 0
    cnt = 1
    # 16진수를 10진수로 바꾸기
    for i in num_16[::-1]:
        if ord('A') <= ord(i) <= ord('Z'):
            num_10 += cnt*(ord(i)-ord('A')+10)
        else:
            num_10 += cnt * int(i)
        cnt *= 16
    # 10진수를 2진수로 바꾸기
    num_2 = ''
    while num_10 != 0:
        num_2 += str(num_10 % 2)
        num_10 = num_10//2
    num_2 = str(num_2[::-1])
    # 자리수 문제에 제시된 대로 만들기
    while len(num_2) < int(N)*4:
        num_2 = '0'+num_2
    print('#{} {}'.format(tc + 1, num_2))
```

- 파이썬 라이브러리 최대로 활용하여 문제 풀기

```python
for tc in range(int(input())):
    N, S = input().split()
    N = int(N)
    print('#{}'.format(tc+1), end=' ')
    t = bin(int(S, 16))
    t = t[2:]
    if len(t) < N * 4:
        t = '0'*(N*4-len(t)) + t
    print(t)
```

- dictionary 이용하여 문제 풀기

```python
hex_number = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def GetResult(n, str_num):
    ret = ''
    for i in range(n):
        number = hex_number[str_num[i]]
        tmp_ret = ''
        for j in range(3, -1, -1):
            bit = str((number >> j) & 1)
            tmp_ret += bit
        ret += tmp_ret
    return ret


for tc in range(int(input())):
    N, input_number = map(str, input().split())
    N = int(N)
    print('#{} {}'.format(tc+1, GetResult(N, input_number)))
```

#### 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 

```python
for tc in range(int(input())):
    N = float(input())
    result = ''
    a = 0.5
    while N != 0:
        # overflow 조건
        if len(result) >= 13:
            result = 'overflow'
            break
        # 2진수 계산하기
        else:
            if N >= a: # 1이 추가되는 경우
                result = result + '1'
                N -= a
            else: # 0이 추가되는 경우
                result = result + '0'
            a *= 0.5
    print('#{} {}'.format(tc+1, result))
```

### 완전 검색

### 탐욕 알고리즘

### 분할 정복

### 백트래킹

### 그래프의 기본과 탐색

### 그래프의 최소 비용 문제

### 문자열 탐색

### 동적 계획법의 소개

### 동적 계획법의 적용

### 동적 계획법의 활용

### NP-Complete

### 근사 알고리즘
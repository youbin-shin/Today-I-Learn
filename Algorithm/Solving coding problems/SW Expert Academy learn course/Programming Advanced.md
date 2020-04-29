# Programming Advanced

### 시작하기

#### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

```python
for tc in range(int(input())):
    N, num = map(str, input().split())
    num_16 = int(num,16) # 16진수로 바꾸기
    num_2 = format(num_16,'b') # 2진수로 바꾸기
    while len(num_2) < int(N)*4: # 문제에 제시된 길이 맞춰주기
        num_2 = '0'+num_2
    print('#{} {}'.format(tc + 1, num_2))
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
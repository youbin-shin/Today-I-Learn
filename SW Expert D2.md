# SW Expert D2

```python
# 1989. 초심자의 회문 검사

tc = int(input())

for i in range(1, tc+1):
    # 입력
    word = input()
    result = 0
    # 계산
    if word == word[::-1]:
        result = 1
    else:
        result = 0

    # 출력
    print('#{} {}'.format(i, result))
```

```python
# 2369. [AtCoder Beginner Contest 073] B. Theater

tc = int(input())

for i in range(tc):
    row = int(input())
    result = 0
    for r in range(row):
        seat1, seat2 = map(int, input().split())
        result += seat2 - seat1 + 1

    print('#{} {}'.format(i+1, result))
```

```python
# 2357. [AtCoder Beginner Contest 073] A. September 9 

tc = int(input())

for i in range(tc):
    num = input()
    for n in num:
        if n == '9':
            result = 'Yes'
            break
    else:
        result = 'No'

    print('#{} {}'.format(i+1, result))
```

```python
# 1945. 간단한 소인수분해

tc = int(input())
for t in range(tc):
    num = int(input())
    factor = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    for i in range(5):
        count = 0
        while True:
            if num % factor[i] == 0:
                count += 1
                num = num//factor[i]
            else:
                result[i] = count
                break
    print('#{} '.format(t+1),end='')
    for j in range(5):
        print('{}'.format(result[j]),end=' ')
    print()
```

```python
# 1986. 지그재그 숫자

tc = int(input())
for t in range(tc):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        if i%2:
            result += i
        else:
            result -= i

    print('#{} {}'.format(t+1,result))
```

```python
# 1926. 간단한 369게임

N = int(input())
N_str = ''
for n in range(1, N+1):
    N_str += str(n) + ' '


N_str = N_str.replace('3','-')
N_str = N_str.replace('6','-')
N_str = N_str.replace('9','-')
for i in range(1, 10):
    b = str(i)+'-'
    N_str = N_str.replace(b, '-')
for i in range(10):
    a = '-'+str(i)
    N_str = N_str.replace(a, '-')
print(N_str)
```

```python
# 2001. 파리 퇴치

tc = int(input())
for t in range(tc):
    N, M = map(int, input().split())
    fly = [[0 for _ in range(N)] for _ in range(N)]
    fkill = 0
    for i in range(N):
        fly[i] = list(map(int, input().split()))

    for a in range(N-M+1):
        for b in range(N-M+1):
            kill = 0
            for m1 in range(M):
                for m2 in range(M):
                    kill += fly[a+m1][b+m2]
                    if fkill < kill:
                        fkill = kill



    print('#{} {}'.format(t+1,fkill))
```

```python
# 1984. 중간 평균값 구하기

tc = int(input())
for t in range(tc):
    num = list(map(int, input().split()))
    num.sort()
    num.pop(0)
    num.pop(-1)
    result = sum(num)/len(num)
    result = int(round(result, 0))


    print('#{} {}'.format(t+1,result))
```

```python
# 1983. 조교의 성적 매기기

tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    K -= 1
    student_lst = [[0 for _ in range(3)] for _ in range(N)]
    score_lst = [0]*N
    clscore_lst = [0]*N

    grade = ['A+', 'A0', 'A-','B+', 'B0', 'B-','C+', 'C0', 'C-','D0']
    for i in range(N):
        student_lst[i] = list(map(int, input().split()))
        score_lst[i] = round(student_lst[i][0]* 0.35 + student_lst[i][1]* 0.45 + student_lst[i][2]* 0.20, 2)
    clscore_lst = list(score_lst)
    clscore_lst.sort(reverse=True)
    gradeidx = clscore_lst.index(score_lst[K])//(N//10)

    print('#{} {}'.format(t+1,grade[gradeidx]))
```

```python
# 1966. 숫자를 정렬하자

tc = int(input())
for t in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    result =''
    for i in range(len(lst)):
        result += str(lst[i]) + ' '

    print('#{} {}'.format(t+1,result))
```

```python

```

```python

```

```python

```

```python

```




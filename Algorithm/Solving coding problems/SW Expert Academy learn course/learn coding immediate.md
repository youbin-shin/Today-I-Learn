```python
# 4864. 문자열 비교
testcase = int(input())

for tc in range(testcase):
    str1 = input()
    str2 = input()
    l1 = len(str1)
    l2 = len(str2)
    i = j = 0
    while i < l2 and j < l1:
        if str2[i] != str1[j]:
            i = i-j
            j = -1
        i = i + 1
        j = j + 1

    if j == l1:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc+1, result))


# 4861 회문
testcase = int(input())

for tc in range(testcase):
    N, M = map(int, input().split())
    lst = [[''] for _ in range(N)]
    for i in range(N):
        lst[i] = list(input())

    # 가로 확인하기
    for j in range(N):
        for i in range(N - M + 1):
            temp = lst[j][i:i+M]
            if temp == temp[::-1]:
                result = ''.join(temp)
                break

    # 세로 확인하기
    for i in range(N):
        for j in range(N - M + 1):
            temp = []
            for k in range(M):
                temp.append(lst[j+k][i])
            if temp == temp[::-1]:
                result = ''.join(temp)
                break


    print('#{} {}'.format(tc+1, result))

# 4865 글자수
testcase = int(input())

for tc in range(testcase):
    str1 = list(set(input()))
    str2 = input()

    cnt = 0
    for i in str1:
        temp_cnt = str2.count(i)
        if temp_cnt > cnt:
            cnt = temp_cnt

    print('#{} {}'.format(tc+1, cnt))



```

```python
# 4869 종이 붙이기

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

T = int(input())

for tc in range(T):
    N = int(input())

    cnt = 0
    b = N//10
    for a in range(N//20+1):
        b2 = b - 2*a
        if b2 < 0:
            b2 = 0
        cnt += factorial(a+b2)*(2**a)/(factorial(a)*factorial(b2))

    print('#{} {}'.format(tc+1,int(cnt)))

# 4866 괄호 검사
testcase = int(input())

for tc in range(testcase):
    line = input()
    stack = [0]*100
    top = -1
    result = 1
    for i in line:
        if i == '('or i == '{':
            top += 1
            stack[top] = i
        elif i == ')':
            if top == -1:
                result = 0
                break
            elif stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                top += 1
                stack[top] = i
        elif i == '}':
            if top == -1:
                result = 0
                break
            elif stack[top] == '{':
                stack[top] = 0
                top -= 1
            else:
                top += 1
                stack[top] = i

        if i == line[-1]:
            if stack == [0]*100:
                result = 1
            else:
                result = 0

    print('#{} {}'.format(tc+1, result))

# 4871 그래프 경로
testcase = int(input())

for tc in range(testcase):
    vertex, line = map(int, input().split())
    G = [[0 for _  in range(vertex+1)] for _ in range(vertex+1)]

    for i in range(line):
        x, y = map(int, input().split())
        G[x][y] = 1

    s, e = map(int, input().split())

    stack = []
    visited = [0]*(vertex+1)
    v = s
    stack.append(v)

    road = 0
    while (len(stack) > 0):
        v = stack.pop(-1)

        if visited[v] != 1:
            visited[v] = 1
            if v == e:
                road = 1
                break

            for w in range(1, len(G[v])):
                if G[v][w] == 1 and visited[w] == 0:
                    stack.append(w)

    print('#{} {}'.format(tc+1, road))

# 4873 반복문자 지우기
testcase = int(input())

for tc in range(testcase):
    str = input()
    stack = [0] * len(str)
    top = -1
    for i in str:
        if top == -1:
            top += 1
            stack[top] = i
        elif stack[top] == i:
            stack[top] = 0
            top -= 1
        else:
            top += 1
            stack[top] = i


    cnt = 0
    for i in range(len(stack)):
        if stack[i] != 0:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))
```


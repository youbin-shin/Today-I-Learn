# Programming  intermediate

### LIST1

#### 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

```python
T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    min = 1000000
    max = 1
    for i in range(N):
        if min > nums[i]:
            min = nums[i]
        if max < nums[i]:
            max = nums[i]
    print('#{} {}'.format(t+1, max-min))
```

#### 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합

```python
# solution 1
for t in range(int(input())):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    Min = 10000000
    Max = -1000000
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += nums[i+j]
        if Max < sum:
            Max = sum
        if Min > sum:
            Min = sum

    print('#{} {}'.format(t+1, Max-Min))
```

```python
# solution 2 _ 슬라이싱 이용
test_case = int(input())

for i in range(test_case):
    N, M = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    sum_list = []

    for idx in range(N-M+1):
        sum_list.append(sum(num_list[idx:idx+M]))

    sum_list = sorted(sum_list)
    print(f'#{i+1} {sum_list[-1]-sum_list[0]}')
```

#### 4834. [파이썬 S/W 문제해결 기본] 1일차 - 숫자 카드

```python
for t in range(int(input())):
    N = int(input())
    card = list(map(int, input()))
    cardcnt = [0] * 10

    for i in card:
        cardcnt[i] += 1

    for i in range(10):
        if max(cardcnt) == cardcnt[i]:
            idx = i

    print('#{} {} {}'.format(t+1, idx, max(cardcnt)))
```

#### 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

```python
for t in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())
    battery = list(map(int, input().split()))
    bus = K
    cnt = 0
    frag = 0

    for i in range(len(battery)-1):
        if battery[i+1] - battery[i] > K:
            break
    else:

        while bus < N:
            if bus in battery:
                bus += K
                cnt += 1
            else:
                for _ in range(K):
                    bus -= 1
                    if bus in battery:
                        bus += K
                        cnt += 1
                        break

    print('#{} {}'.format(t, cnt))
```

### LIST2

#### 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

```python
for t in range(int(input())):
    board = [[0 for _ in range(10)] for _ in range(10)]
    for n in range(int(input())):
        x1, y1, x2, y2, val = map(int, input().split())

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] += val
    ans = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] > 2:
                ans += 1
    print('#{} {}'.format(t+1, ans))
```

#### 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

```python
def binarySearch(all, page):
    cnt = 0
    l = 1
    r = all
    c = (l+r)>>1
    while page != c:
        if page > c:
            l = c
            cnt += 1
        else:
            r = c
            cnt += 1
        c = (l+r)>>1
    return cnt

for t in range(int(input())):
    P, A, B = map(int, input().split())
    ans = 0
    if binarySearch(P, A) > binarySearch(P, B):
        ans = 'B'
    elif binarySearch(P, A) < binarySearch(P, B):
        ans = 'A'
    print('#{} {}'.format(t+1, ans))
```

#### 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬 

```python
for t in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    result = []
    for i in range(10):
        if i%2: # 홀수행 작은수
            result.append(str(min(nums)))
            nums.remove(min(nums))
        else:
            result.append(str(max(nums)))
            nums.remove(max(nums))

    result = ' '.join(result)
    print('#{} {}'.format(t+1,result))
```

#### 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

```python
tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())
    A = list(range(1,13))
    cnt = 0

    for i in range(1<<len(A)):
        sum = 0
        subset = []
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(A[j])
        for k in range(len(subset)):
            sum += subset[k]
        if sum == K and len(subset) == N:
            cnt += 1

    print('#{} {}'.format(t+1, cnt))
```

### String

#### 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

```python
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
```

#### 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

```python
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
```

#### 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

```python
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
# teacher solution 1
for t in range(int(input())):
    str1 = input()
    str2 = input()
    dict = {}.fromkeys(str1, 0) # Dictionary 생성

    for ch in str2:
        if ch in dict:
            dict[ch] += 1

    print('#{} {}'.format(t+1, max(dict.values())))
```

```python
# teacher solution 2
for t in range(int(input())):
    str1 = input()
    str2 = input()

    cnt = [0] * 138 # 문자를 배열의 인덱스로 사용한다.
    for ch in str2:
        cnt[ord(ch)] += 1

    ans = 0
    for ch in str1:
        if cnt[ord(ch)]:
            ans = max(ans, cnt[ord(ch)])
    print('#{} {}'.format(t+1, ans))
```

### Stack1

#### 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

```python
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
```

#### 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

```python
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
```

#### 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

```python
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
```

#### 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

```python
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

### Stack2

#### 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

```python
T = int(input())
for t in range(T):
    Fourth = list(map(str, input().split()))
    math = ['+', '-', '*', '/']
    stack = []

    finalresult = 0
    result = 0
    for f in Fourth:
        if f not in math and f != '.': # 숫자는 스택에 넣는다.
            stack.append(f)
        elif f in math and len(stack) >= 2:
            num2 = int(stack.pop(-1))
            num1 = int(stack.pop(-1))

            if f == math[0]:
                result = num1 + num2
            elif f == math[1]:
                result = num1 - num2
            elif f == math[2]:
                result = num1 * num2
            elif f == math[3]:
                result = num1 / num2
            stack.append(result)

        elif f == '.' and len(stack) == 1:
            finalresult = int(stack.pop(-1))
            break
        else:
            finalresult = 'error'
            break


    print('#{} {}'.format(t+1, finalresult))
```

#### 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

```python
def notWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False

T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dir = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    stack = []

    # 출발점 찾기
    frag = 1
    for i in range(N):
        if frag == 0:
            break
        for j in range(N):
            if maze[i][j] == 2:
                sx, sy = i, j
                flag = 1
                break

    v = [sx, sy]
    stack.append(v)
    result = 0

    while (len(stack) > 0):
        x, y = stack.pop()

        if result == 1:
            break

        if visited[x][y] != 1:
            visited[x][y] = 1

            for i in range(4):
                nx = x + dir[i][0]
                ny = y + dir[i][1]

                if notWall(nx, ny) == True:
                    if maze[nx][ny] == 0 and visited[nx][ny] == 0:
                        stack.append([nx, ny])

                    elif maze[nx][ny] == 3:
                        result = 1
                        break

    print('#{} {}'.format(t+1, result))
```

#### 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

```python

```

#### 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

```python

```

### 큐 (Queue)

#### 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

```python
for t in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        lst.append(lst.pop(0))
    print('#{} {}'.format(t+1, lst[0]))
```

#### 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

```python
for t in range(int(input())):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = [[0,0]] * N
    i = -1
    result = []
    while len(oven):
        oven[0][1] = oven[0][1] // 2
        if oven[0][1] == 0:
            result.append(oven[0][0])
            oven.pop(0)
            i += 1
            if i < M:
                oven.append([i, pizza[i]])
        else:
            oven.append(oven.pop(0))

    print('#{} {}'.format(t+1,result[-1]+1))
```

#### 5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

```python
for tc in range(int(input())):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    queue = []
    G = [[] for _ in range(V + 1)] # 인접 리스트
    for _ in range(E):
        e1, e2 = map(int, input().split())
        # 방향이 없기에 두번 추가해주기
        G[e1].append(e2)
        G[e2].append(e1)
    start, goal = map(int, input().split())
    queue.append(start)
    visited[start] = True

    result = 1
    while queue:
        t = queue.pop(0)
        if t == goal:
            result = visited[t]
            break
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1

    print('#{} {}'.format(tc+1,result-1))
```

#### 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

```python
# solution 1
for tc in range(int(input())):
    # 초기 상태 설정
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = []

    # 시작점 찾기
    frag = 0
    for i in range(N):
        if frag == 1:
            break
        for j in range(N):
            if maze[i][j] == 2:
                frag = 1
                start = [i, j]
                visited[i][j] = 1
                break
	
    # queue
    result = N * N
    queue.append(start)
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while queue:
        t = queue.pop(0)
        for d in range(4):
            ix = t[0] + dir[d][0]
            iy = t[1] + dir[d][1]
            if 0 <= ix <N and 0<=iy<N and maze[ix][iy] != 1:
                if maze[ix][iy] == 3:
                    result = min(visited[t[0]][t[1]], result)
                if not visited[ix][iy]:
                    queue.append([ix, iy])
                    visited[ix][iy] = visited[t[0]][t[1]] + 1
    if result == N*N:
        result = 1

    print('#{} {}'.format(tc+1, result-1))
```

```python
# solution 2
# queue.pop 하여 도착점 확인! (이 방법을 권장함)
for tc in range(int(input())):
    # 초기 상태 설정
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    queue = []

    # 시작점 찾기
    frag = 0
    for i in range(N):
        if frag == 1:
            break
        for j in range(N):
            if maze[i][j] == 2:
                frag = 1
                start = [i, j]
                visited[i][j] = 1
                break

    # queue
    result = N * N
    queue.append(start) # enqueue 부분
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while queue:
        t = queue.pop(0)
        if maze[t[0]][t[1]] == 3:
            result = min(visited[t[0]][t[1]], result)
        for d in range(4):
            ix = t[0] + dir[d][0]
            iy = t[1] + dir[d][1]
            if 0 <= ix <N and 0<=iy<N and maze[ix][iy] != 1:

                if not visited[ix][iy]:
                    queue.append([ix, iy])
                    visited[ix][iy] = visited[t[0]][t[1]] + 1
    if result == N*N:
        # 도착점 못 찾는 경우
        result = 2

    print('#{} {}'.format(tc+1, result-2))
    # 처음 시작값 2를 발견했을 때 visited에 1을 넣었고
    # 3에 도착한 것도 1을 추가해줬기에 -2를 해줘야한다.
```

![image-20200403173354856](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200403173354856.png)

![image-20200403173403527](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200403173403527.png)

![image-20200403173454892](C:\Users\youbi\AppData\Roaming\Typora\typora-user-images\image-20200403173454892.png)

### Linked List

#### 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가

```python
# Linked List

class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소

class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.tail = None # 마지막 노드
        self.size = 0  # 노드의 수

    def insert_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조

def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()

def insertLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # else 문 뒤 코드 순서 바뀌면 안된다!!
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def insertAt(lst, idx, new): # idx : 인덱스 값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우, idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        # 중간에 추가하는 경우 (head, tail 변화 X)
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def search(lst, target):
    cur = lst.head
    for _ in range(target):
        cur = cur.next
    return cur.data

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    lst = LinkedList()
    putlst = list(map(int, input().split()))
    for i in range(len(putlst)):
        insertLast(lst, Node(putlst[i]))
    for m in range(M):
        idx, new = map(int, input().split())
        insertAt(lst, idx, Node(new))

    # printList(lst)
    result = search(lst, L)
    print('#{} {}'.format(tc+1, result))
```

```python
# list 참고용
for tc in range(int(input())):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    for m in range(M):
        idx, num = map(int, input().split())
        lst.insert(idx, num)
    print('#{} {}'.format(tc+1, lst[L]))
```

#### 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

```python
# linked list
class Node:
    def __init__(self, d=0, n=None):
        self.data = d  # 정수 값
        self.next = n  # 다음 노드 주소

class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드
        self.tail = None # 마지막 노드
        self.size = 0  # 노드의 수

    def insert_front(self, item):
        if self.is_empty():  # 첫 노드로 삽입
            self.head = self.Node(item, None)  # head가 새 노드 참조

def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head
    while cur is not None: # while cur.next is not None: 이면 4까지 출력
        print(cur.data, end=' ')
        cur = cur.next
    print()

def insertLast(lst, new): # new : 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        # else 문 뒤 코드 순서 바뀌면 안된다!!
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new
    lst.size += 1

def insertAt(lst, idx, new): # idx : 인덱스 값
    # 빈리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst, new)
    # 마지막 추가하는 경우, idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        # 중간에 추가하는 경우 (head, tail 변화 X)
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        new.next = cur
        pre.next = new
        lst.size += 1

def search(lst, target):
    cur = lst.head
    for _ in range(target):
        cur = cur.next
    return cur.data

def change(lst, idx, num):
    cur = lst.head
    for _ in range(idx):
        cur = cur.next
    cur.data = num

def deleteLast(lst):
    if lst.head is None: return
    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next
    if pre is None: # list 한개일 경우 pre.next 에서 오류나기에 걸러주기
        lst.head = lst.tail = None
    else:
        pre.next = None
        lst.tail = pre
        lst.size -= 1


def deleteFirst(lst):
    if lst.head is None: return
    # 노드가 1개 일 경우 주의하기
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1


def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx >= lst.size:
        deleteLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        lst.size -= 1


for tc in range(int(input())):
    N, M, L = map(int, input().split())
    lst = LinkedList()
    putlst = list(map(int, input().split()))
    for i in range(len(putlst)):
        insertLast(lst, Node(putlst[i]))
    for m in range(M):
        plus = list(map(str, input().split()))
        plus[1] = int(plus[1])
        if len(plus) == 3:
            plus[2] = int(plus[2])
            if plus[0] == 'I':
                insertAt(lst, plus[1], Node(plus[2]))
            else:
                change(lst, plus[1], plus[2])
        else:
            deleteAt(lst, plus[1])
    if lst.size <= L:
        result = -1
    else:
        result = search(lst, L)
    print('#{} {}'.format(tc + 1, result))
```

```python
# list 참고용
for tc in range(int(input())):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    for m in range(M):
        plus = list(map(str, input().split()))
        plus[1] = int(plus[1])
        if len(plus)==3:
            if plus[0]=='I':
                lst.insert(plus[1], plus[2])
            else:
                lst[plus[1]] = plus[2]
        else:
            lst.pop(plus[1])
    if len(lst) <= L:
        result = -1
    else:
        result = lst[L]
    print('#{} {}'.format(tc+1, result))
```

### 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기

```python
# double linked list
class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: # 마지막위치에 추가 (prev보다 먼저 해야함)
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None: # cur == lst.head 맨앞에 추가
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else: # 중간
            prev = cur.prev # prev 변수에 넣은 것 뿐!! 복잡해져서
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)


def printList(lst):
    if lst.head is None: return
    else:
        cur = lst.tail
        cnt = 0
        while cur is not None:
            if cnt == 10:
                break
            cnt += 1
            print(cur.data, end=' ')
            cur = cur.prev
        print()


for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = LinkedList()
    arr = list(map(int, input().split()))
    addList(lst, arr)

    for m in range(M-1):
        temp = list(map(int, input().split()))
        addList(lst, temp)
    print('#{} '.format(tc+1), end='')
    printList(lst)
```

```python
# slicing
for tc in range(int(input())):
    # input
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split())) # 처음 거는 인풋 받아서 만들고
    for _ in range(M-1): # 그 다음부터는 이전 거랑 비교
        temp_numbers = list(map(int, input().split()))
        for idx in range(len(numbers)):
            if numbers[idx] > temp_numbers[0]:
                numbers[idx:idx] = temp_numbers
                break
        else: # break에 걸리지 않은 경우
            numbers += temp_numbers
    print("#%d %s" %(tc+1, ' '.join(list(map(str,numbers[::-1][:10])))))
```

```python
# list 참고용
# 크기가 크면, ValueError: too many values to unpack 오류 발생
for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for m in range(M):
        temp = list(map(int, input().split()))
        for n in range(len(lst)):
            if lst[n] > temp[0]:
                for i in range(len(temp)):
                    lst.insert(n+i, temp[i])
            elif n == len(lst)-1:
                for i in range(len(temp)):
                    lst.append(temp[i])
    result = list(map(str, lst[::-1]))
    print('#{}'.format(tc+1), end=' ')
    print(' '.join(result[:10]))
```

#### 5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호

```python
# 원형 이중연결 리스트
# next, prev 에 None이 없다!!
# tail은 따로 저장하지 않지만 head.prev 은 tail을 가리킴!

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.size = 0

def printList(lst): # lst : LinkedList 객체
    if lst.head is None: # 빈리스트 ( 항상 고려하고 주의하자! )
        return
    cur = lst.head.prev
    for _ in range(min(lst.size, 10)):
        print(cur.data, end=' ')
        cur = cur.prev
    print()

def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1

for tc in range(int(input())):
    lst = LinkedList()
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    for val in arr:
        addLast(lst, Node(val))

    cur = lst.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new # 새로 추가된 위치를 시작위치로 재설정
        lst.size += 1
    print('#{}'.format(tc+1), end=' ')
    printList(lst)
```

```python
# slicing
tc = int(input())
for t in range(1, tc + 1):
    N, M, K = map(int, input().split())
    base_list = list(map(int, input().split()))
    idx = 0
    for i in range(K):
        idx += M
        if idx > len(base_list):
            idx = idx - len(base_list)
        if idx == len(base_list):
            base_list.append(base_list[0] + base_list[idx - 1])
        else:
            base_list[idx:0] = [base_list[idx - 1] + base_list[idx]]
    result = base_list[-1:-11:-1]
    result = ' '.join(map(str, result))
    print('#{} {}'.format(t, result))
```

### Tree

#### 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

```python
def func(v):
    global cnt
    if v == 0: return
    func(L[v])
    cnt += 1
    func(R[v])

for t in range(int(input())):
    E, N = map(int, input().split())
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    info = list(map(int, input().split()))
    for i in range(0, len(info), 2):
        parent, child = info[i], info[i + 1]
        if L[parent]: R[parent] = child
        else: L[parent] = child

    cnt = 0
    func(N)
    print('#{} {}'.format(t+1, cnt))
```

#### 이진탐색

```python
def makeT(n):
    global idx
    global N
    if n <= N:
        makeT(n*2) # 왼쪽 서브트리 방문
        tree[n] = idx # 중위 순회로 현재 노드값 저장
        idx += 1
        makeT(n*2+1) # 오른쪽 서브트리 방문


for tc in range(int(input())):
    N = int(input())
    idx = 1
    tree = [0 for _ in range(N+1)] # 리스트를 이용한 완전 이진 트리 저장장
   makeT(1)
    print('#{} {} {}'.format(tc+1, tree[1], tree[N//2]))
```

#### 이진 힙

```python
def enq(n):
    global last
    last += 1 # 마지막 노드번호 증가
    c = last # 마지막 노드를 자식 노드로
    p = c//2 # 부모 노드 번호 계산
    q[last] = n # 마지막 노드에 값 저장
    while c>1 and q[p] > q[c]: # 루트가 아니고 부모 노드의 값이 더 크면
        t = q[p] # 저장된 값 바꿈
        q[p] = q[c]
        q[c] = t
        c = p # 부모를 새로운 자식 노드로
        p = p//2

def find(): # 마지막 노드의 조상 노드 찾기
    global N
    c = N
    p = c//2
    s = 0
    while p > 0:
        s += q[p] # 조상 노드 값을 더함
        p = p//2
    return s

for tc in range(int(input())):
    N = int(input())
    last = 0 # 노드가 하나도 없는 상태
    q = [0 for i in range(N+1)] # 이진 힙 구현을 위한 리스트 생성    
    L = list(map(int, input().split()))

    for i in range(N): # 힙에 저장
        enq(L[i])
    print('#{} {}'.format(tc+1, find()))
```

#### 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

```python
# list 이용
for t in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2) # 0 인덱스 때문에 +1, 리프 노드의 오른쪽 노드가 없을 경우 IndexError 제거를 위해 +1
    for _ in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    idx = N - M
    while idx > 0:
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
        idx -= 1
    print('#{} {}'.format(t+1, tree[L]))
```


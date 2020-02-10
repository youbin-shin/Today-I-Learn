# jungol.co.kr

### Beginner Coder

```python
# 1291 구구단
while True:
    s, e = map(int, input().split())
    if (2 <= s <= 9) and (2 <= e <= 9):
        break
    else:
        print('INPUT ERROR!')

if s <= e:
    for i in range(1, 10):
        for j in range(s, e+1):
            if len(str(i*j)) == 1:
                ij = ' ' + str(i*j)
            else:
                ij = str(i*j)
            print('{} * {} = {}   '.format(j, i, ij),end='')
        print()

else:
    for i in range(1, 10):
        for j in range(s, e -1, -1):
            if len(str(i*j)) == 1:
                ij = ' ' + str(i*j)
            else:
                ij = str(i*j)
            print('{} * {} = {}   '.format(j, i, ij),end='')
        print()
```

```python
# 1341 구구단 2
s, e = map(int, input().split())

if s <= e:
    for j in range(s, e+1):
        for i in range(1, 10):
            if len(str(i*j)) == 1:
                ij = ' ' + str(i*j)
            else:
                ij = str(i*j)
            print('{} * {} = {}   '.format(j, i, ij),end='')
            if i % 3 == 0:
                print()
        print()

else:
    for j in range(s, e -1, -1):
        for i in range(1, 10):
            if len(str(i*j)) == 1:
                ij = ' ' + str(i*j)
            else:
                ij = str(i*j)
            print('{} * {} = {}   '.format(j, i, ij),end='')
            if i % 3 == 0:
                print()

        print()
```

```python
# 1303 숫자사각형 1
n, m = map(int, input().split())

for i in range(1, n*m+1):
    print('{}'.format(i), end=' ')
    if i%m == 0:
        print()

```

```python
# 1856 숫자사각형 2
n, m = map(int, input().split())
cnt = 1
row = 0
while cnt <= n:
    if cnt%2:
        for i in range(row+1, row+1+m):
            print('{}'.format(i),end=' ')
            row = i
        cnt += 1
        print()
    else:
        for i in range(row+m, row,-1):
            print('{}'.format(i),end=' ')
            if row < i:
                row = i
        cnt += 1
        print()
```

```python
# 1304 숫자사각형 3
n = int(input())

for i in range(1, n+1):
    result = i
    for j in range(n):
        print('{}'.format(i + n*j), end=' ')
    print()
```

```python
# 2046 숫자사각형 4
n, m = map(int, input().split())

if m==1:
    for j in range(1, n+1):
        for _ in range(n):
            print('{}'.format(j), end=' ')
        print()

elif m==2:
    result = ''
    bresult = ''
    for i in range(1, n+1):
        result += str(i) + ' '
        bresult += str(n-i+1) + ' '
    for j in range(n):
        if j%2 == 0:
            print(result)
        else:
            print(bresult)

else:
    for j in range(1, n+1):
        for i in range(n):
            result = j + j * i
            if i != 0 and len(str(result))==1:
                i = ' '+str(i)
            print('{}'.format(result), end=' ')
        print()
```

```python
# 1307 문자사각형 1
text =[]
for i in range(65, 91):
    text.append(chr(i))

n = int(input())

for i in range(n):
    result = n * n - i
    for _ in range(n):
        print('{}'.format(text[(result-1)%26]), end=' ')
        result -= n
    print()
```

```python
# 1314 문자사각형 2 
#####답x
text =[]
for i in range(65, 91):
    text.append(chr(i))

n = int(input())

for i in range(n):
    result = i+1
    for _ in range(n):
        print('{}'.format(text[(result-1)%26]), end=' ')
        result += n
    print()
```

```python
# 1338 문자사각형 3
```

```python
# 1339 문자사각형 4
```

```python
# 1692 곱셈
a = int(input())
b = int(input())
print('{}'.format((b%10)*a))
print('{}'.format(((b%100-b%10)//10)*a))
print('{}'.format((b//100)*a))
print('{}'.format(a*b))
```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```

```python

```
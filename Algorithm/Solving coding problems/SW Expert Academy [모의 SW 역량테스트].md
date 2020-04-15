# SW Expert Academy [모의 SW 역량테스트] 

### 5658. 보물상자 비밀번호

```python
for tc in range(int(input())):
    N, K = map(int, input().split())
    n = N//4
    nums = list(input())
    result = []
    for _ in range(n+1):
        for n1 in range(0, N, n):
            cal = 0
            cnt = 1
            for n2 in range(n1+n-1, n1-1, -1):
                if nums[n2] in 'ABCDEF': # A ~ F
                    cal += cnt * (ord(nums[n2]) - 55)
                else:
                    cal += cnt * int(nums[n2])
                cnt *= 16
                if n2 == n1 and cal not in result:
                    result.append(cal)
        nums.insert(0, nums.pop())

    result.sort(reverse=True)
    print('#{} {}'.format(tc+1, result[K-1]))
```


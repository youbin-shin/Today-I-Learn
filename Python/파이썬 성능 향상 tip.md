# 파이썬 성능 향상 :honey_pot:tip

> https://wiki.python.org/moin/PythonSpeed/PerformanceTips

### Sorting정렬

- 기본 파이썬 객체의 목록을 정렬하는 것은 일반적으로 매우 효율적이다. 

#### Schwartzian Transfrom (DSU, DecorateSortUndecorate)

- 기본 구조

  각 튜플의 n번째 필드를 기준으로 정렬하려는 튜플 목록이 있다고 가정한다.

  ```python
  def sortby(somelist, n):
      nlist = [(x[n], x) for x in somelist]
      nlist.sort()
      return [val for (key, val) in nlist]
  ```

  현재 목록 정렬 방법(정렬 위치)의 동작을 쉽게 일치시킬 수 있다. 

  ```python
  def sortby_inplace(somelist, n):
      somelist[:] = [(x[n], x) for x in somelist]
      somelist.sort()
      somelist[:] = [val for (key, val) in somelist]
      return
  ```

- 예제 코드 1

  ```python
  >>> somelist = [(1, 2, 'def'), (2, -4, 'ghi'), (3, 6, 'abc')]
  >>> somelist.sort()
  >>> somelist
  [(1, 2, 'def'), (2, -4, 'ghi'), (3, 6, 'abc')]
  >>> nlist = sortby(somelist, 2)
  >>> sortby_inplace(somelist, 2)
  >>> nlist == somelist
  True
  >>> nlist = sortby(somelist, 1)
  >>> sortby_inplace(somelist, 1)
  >>> nlist == somelist
  True
  ```

- 예제 코드 2

  - 선택적 키 매개 변수를 추가하여 변환을 훨씬 쉽게 사용 가능하다.

    ```python
    # E.g. n = 1
    n = 1
    import operator
    nlist.sort(key=operator.itemgetter(n))
    # use sorted() if you don't want to sort in-place:
    # sortedlist = sorted(nlist, key=operator.itemgetter(n))
    ```

  - 원래 항목은 정렬에 사용되지 않으며 반환된 키만 사용된다.

    ```python
    # E.g. n = 1
    n = 1
    nlist = [(x[n], i, x) for (i, x) in enumerate(nlist)]
    nlist.sort()
    nlist = [val for (key, index, val) in nlist]
    ```

    
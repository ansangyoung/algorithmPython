# BinarySearch

### 정의
이진 검색 알고리즘(binary search algorithm)은 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.  

### 방식
처음 중간의 값을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식을 채택하고 있다.  
처음 선택한 중앙값이 만약 찾는 값보다 크면 그 값은 새로운 최댓값이 되며, 작으면 그 값은 새로운 최솟값이 된다.  
검색 원리상 정렬된 리스트에만 사용할 수 있다는 단점이 있지만, 검색이 반복될 때마다 목표값을 찾을 확률은 두 배가 되므로 속도가 빠르다는 장점이 있다.

### 요약
> 정렬된 리스트 기반, 복잡도는 O(logN)

```
//의사코드
BinarySearch(A[0..N-1], value, low, high) {
  if (high <= low)
    return -1 // not found
  mid = (low + high) / 2
  if (A[mid] > value)
    return BinarySearch(A, value, low, mid-1)
  else if (A[mid] < value)
    return BinarySearch(A, value, mid+1, high)
  else
    return mid // found
}
```
알고리즘 문제 풀이를 적용하기 위해서는 의사코드를 기반으로 유효성검사 로직, 조건문의 위치, low, mid, high 등을 커스터마이징하여 구현해야한다.  
예를들어 단순히 의사코드에서는 함수의 자료의 개수가 2개일 경우, not found로 끝날 수 있다.

### 추천 문제
[BAEKJOON 11561 징검다리](https://www.acmicpc.net/problem/11561)

1. 강엔 1번부터 시작해 2번, 3번, ... , N번 징검다리가 차례대로 놓여 있다.
2. 첫 징검다리는 점프해서 아무 것이나 밟을 수 있다. 이 점프가 첫 점프이다.  
3. 두 번째 점프부터는 이전에 점프한 거리보다 1 이상 더 긴 거리를 뛰어야만 한다.  
4. N번 징검다리는 반드시 밟아야 한다.(최종 밟아야 하는 징검다리)
5. 승택이가 위의 규칙을 지키며 강을 건널 때, 밟을 수 있는 징검다리의 최대 수는 몇 개일까?

[문제풀이](https://github.com/ansangyoung/algorithmPython/blob/dev_ssffwert/Search/baekJoon11561.py)

### Reference
[위키백과 이진검색 알고리즘](https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%A7%84_%EA%B2%80%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)8)

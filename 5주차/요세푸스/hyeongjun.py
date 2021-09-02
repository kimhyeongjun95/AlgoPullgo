# 1번부터 n번 / n명
# 순서대로 k번째 사람 제거 -> 모두 제거될때까지 반복
# 제거되는 순서 : 요세푸스 순열
# 7, 3
# 1, 2, 3, 4, 5, 6, 7 -> 3이 제일 앞에 있을때 그 뒤로 3번.. 이런 식인듯
# 4, 5, 6, 7, 1, 2
# 7, 1, 2, 4, 5
# 4, 5, 7, 1
# 1, 4, 5
# 1, 4
# 4
# <3, 6, 2, 7, 5, 1, 4> 왼쪽에서 빠져나가는거니 큐로 구현하면 될거같다.

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
numbers = deque(i for i in range(1, n+1))

# answer = '' # <, >를 받아줘야하니 문자열로 받아볼까?? -> 마지막 쉼표가 거슬림
answer = []
while numbers:
    for _ in range(k-1):
        numbers.append(numbers.popleft())
    answer.append(numbers.popleft())

answer = ', '.join(map(str, answer))
print('<' + answer + '>')
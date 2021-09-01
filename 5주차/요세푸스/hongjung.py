import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

people = deque(range(1, N+1))

result = []
while people:
    for _ in range(K-1):
        people.append(people.popleft())
    result.append(people.popleft())

result = ', '.join(list(map(str, result)))
print('<', end="")
print(result, end="")
print('>')
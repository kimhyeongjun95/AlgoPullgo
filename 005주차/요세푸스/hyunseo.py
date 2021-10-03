from collections import deque

N, K = map(int, input().split())

numbers = deque(i for i in range(1, N+1))
result = []

n = 1
while numbers:
    if n%K:
        numbers.append(numbers.popleft())
    else:
        result.append(numbers.popleft())
    
    n += 1

print('<', end='')
for i in range(N):
    if i == N-1:
        print('{}>'.format(result[i]))
    else:
        print(result[i], end=', ')
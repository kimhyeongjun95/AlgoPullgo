# 백준 17471 게리맨더링

# N개의 구역
# 각 구역은 두 선거구 중 하나에 포함
# 한 선거구에 포함된 구역 -> 모두 연결

# 두 선거구 인구의 차이 최소화 -> 최솟값 구하기
# 나눌 수 없으면 -1

# 1. 선거구를 2개로 나눈다.
# 1-1. 모든 경우의 수 만들기

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

def hello(roamer):
    visited = [0] * (n+1)
    queue = deque([roamer[0]])
    # 처음 방문처리
    visited[roamer[0]] = 1
    total = 0
    while queue:
        x = queue.popleft()
        # 인구수 더하기
        total += populations[x]
        for i in connect[x]:
            # 경우의 수에 들어가있고 방문안한 곳
            if i in roamer and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
    
    length = len([i for i in visited if i == 1])
    return total, length

n = int(input())
# 인구 구역
populations = [0]
populations.extend(list(map(int, input().split())))

# 인접한 구역의 정보
connect = [0]
arr = [list(map(int, input().split())) for _ in range(n)]
for i in arr:
    connect.append(i[1:])

result = float('inf')
result_base = float('inf')
# 선거구가 2개로 나눠지기에 n//2+1 까지만 확인
for i in range(1, (n//2)+1):
    combos = list(combinations(range(1, n+1), i))
    for combo in combos:
        combo2 = [i for i in range(1, n+1) if i not in combo]
        count1, len1 = hello(combo)
        count2, len2 = hello(combo2)
        if len1 + len2 == n:
            result = min(result, abs(count1 - count2))

if result == result_base:
    print(-1)
else:
    print(result)
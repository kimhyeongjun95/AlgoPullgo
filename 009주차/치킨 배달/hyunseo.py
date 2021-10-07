# 백준 15686 치킨 배달
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

result = []
for now_chicken in combinations(chicken, M):
    temp = 0
    for i, j in house:
        min_dist = float('inf')
        for k, l in now_chicken:
            dist = abs(i-k) + abs(j-l)
            min_dist = min(dist, min_dist)

        temp += min_dist
    
    result.append(temp)

print(min(result))
import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))


result = []
for i in list(combinations(chicken, M)):
    city_chicken_dist = 0
    for hx, hy in house:
        dist_lst = []
        for sx, sy in i:
            dist = abs(hx-sx) + abs(hy-sy)
            dist_lst.append(dist)
        city_chicken_dist += min(dist_lst)
    result.append(city_chicken_dist)
print(min(result))

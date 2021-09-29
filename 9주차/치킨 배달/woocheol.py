# 15686번 치킨배달

from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append([i, j])
        elif graph[i][j] == 1:
            house.append([i, j])

ans = float('inf')
for chickens in combinations(chicken, m):
    temp = 0
    for h in house:
        temp += min(abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in chickens)
        if temp > ans:
            break
    ans = min(temp, ans)

print(ans)

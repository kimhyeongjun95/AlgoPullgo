from itertools import combinations

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 2:
            chickens.append((i,j))
        if matrix[i][j] == 1:
            houses.append((i,j))
ans = 9999999
for choices in combinations(chickens,M):
    total = 0
    for house in houses:
        r, c = house
        min_dist = 50
        for choice in choices:
            i, j = choice
            dist = abs(r-i)+abs(c-j)
            min_dist = min(min_dist, dist)
        total += min_dist
    ans = min(ans, total)
print(ans)


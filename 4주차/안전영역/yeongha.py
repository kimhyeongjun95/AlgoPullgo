import sys
import copy
sys.setrecursionlimit(10**9) # 재귀 한도 제한 높이기

def dfs(rain, i, j):
    city_copy[i][j] = 0
    dxy = [(0,1),(1,0),(0,-1),(-1,0)] # 오른쪽, 아래, 왼쪽, 위

    for dx, dy in dxy:
        x, y = i + dx, j + dy
        if -1 < x < N and -1 < y < N and city_copy[x][y] > rain:
            dfs(rain, x, y)

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
numbers = []
i = 0
totals = []
while True:
    total = 0
    city_copy = copy.deepcopy(city)
    for r in range(N):
        for c in range(N):
            if city_copy[r][c] > i:
                total += 1
                dfs(i, r, c)
    if total == 0:
        break
    totals.append(total)
    i+=1
print(max(totals))
# 백준 14502 연구소

# 바이러스 확산을 막기위한 벽 세우기
# 연구소 : N x M
# 상하좌우로 바이러스 이동

# 0 빈칸, 1 벽, 2 바이러스
# 바이러스는 2 <= 바이러스 <= 10
# 세울수 있는 벽의 개수는 3개, 반드시 3개를 세워야 함
# 바이러스가 퍼진 이후 0의 갯수(최댓값) 구하기

# DFS / BFS
# 3개의 함수 만들기
# 1. 바이러스 분포
# 2. 영역 계산
# 3. 벽 만들기

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 바이러스 확산
def spread(x, y, temp): 
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < n and  -1 < ny < m:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    queue.append((nx, ny))

# 영역 계산
def caculate(temp):
    result = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                result += 1

    return result

# 벽 세우기, 브루트 포스로 풀자
def wall(combi, virus):
    answer = []
    for combo in combi:
        
        # 1. 첫 번째 복사방법 -> 이게 훨씬빠름
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        
        # 2. 두 번째 복사방법
        # temp = copy.deepcopy(lab)

        # 3개의 벽 경우의 수
        temp[combo[0][0]][combo[0][1]] = 1
        temp[combo[1][0]][combo[1][1]] = 1
        temp[combo[2][0]][combo[2][1]] = 1

        for x, y in virus:
            spread(x, y, temp)
        
        # 벽 돌려놓기 -> 
        # 벽을 돌려놓고 바이러스를 돌려놓는것보다 새로 생성이..
        # lab[i[0][0]][i[0][1]] = 0
        # lab[i[1][0]][i[1][1]] = 0
        # lab[i[2][0]][i[2][1]] = 0
        
        result = caculate(temp) # 영역 계산
        answer.append(result)
    return answer

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]

blank = []
virus = []
for i in range(n): 
    for j in range(m):
        if lab[i][j] == 0: # 0인 지역 좌표 저장
            blank.append((i, j))
        if lab[i][j] == 2: # 2인 지역 좌표 저장
            virus.append((i, j))
        
combi = combinations(blank, 3)

answer = wall(combi, virus)
print(max(answer))
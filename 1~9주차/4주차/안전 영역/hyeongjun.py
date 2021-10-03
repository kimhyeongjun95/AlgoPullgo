# # n x n 2차원 배열
# # height 몇 이하는 물에 잠김
# # 물에 잠기지 않는 영역, dfs 또는 bfs 문제인듯
# # 물에 잠기지 않는 안전한 영역 최대 개수
# # 2 <= n <= 100
# # 1 <= 높이 <= 100 -> find 높이
# import sys
# sys.setrecursionlimit(100000) # 재귀제한 해제

# def find_height(x, y, height):
#     for i in range(4):
#         visited[x][y] = 1
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if -1 < nx < n and -1 < ny < n and area[nx][ny] > height and visited[nx][ny] == 0: # 스택으로 2시간동안 구현 실패 ㅠ (이 and 부분들 )따로보면 안되는듯
#             find_height(nx, ny, height)

#     # if x <= -1 or x >= n or y <= -1 or y >= n:
#     #     return False # 필수조건

#     # if area[x][y] > height and visited[x][y] == 0: # area[x][y]가 낮지말고 높아야한다!@!@!@!@!@!@!!!!!!! 회색을 세는게 아니라 흰색을 세는것
#     #     visited[x][y] = 1
#     #     find_height(x-1, y, height)
#     #     find_height(x+1, y, height)
#     #     find_height(x, y+1, height)
#     #     find_height(x, y-1, height)
#     #     return True
#     # return False

# n = int(input())
# area = [list(map(int, input().split())) for _ in range(n)]

# ''''''
# temp = [] # 최댓값 리스트
# for i in range(n):
#     temp.append(max(area[i]))
# idx = max(temp) # 최대 높이 구해서 연산횟수 줄이기
# ''''''''

# # 좌 상 우 하
# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# answer = []

# for height in range(1, idx+1):# height가 최대 높이에 도달하기 이전까지
#     count = 0
#     visited = [[0] * n for _ in range(n)] # 2차원 행렬 매번 새로 만들어줘야함
#     for i in range(n):
#         for j in range(n):
#             if area[i][j] > height and visited[i][j] == 0:
#                 count += 1
#                 find_height(i, j, height)

#     answer.append(count)
    
# print(max(answer))
    
# #     if count > 0: result.append(count)
    
# # if result:
# #     print(max(result))
# # else:
# #     print(0)

import sys
sys.setrecursionlimit(100000)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_area(x, y, height):
    # for i in range(4):
    #     visited[x][y] = 1
    #     nx = x + dx[i]
    #     ny = y + dy[i]

    #     if -1 < nx < n and -1 < ny < n and area[nx][ny] > height and visited[nx][ny] == 0:
    #         find_area(nx, ny, height)

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

temp = []
for i in area:
    temp.append(max(i))
max_height = max(temp)

answer = []
for height in range(max_height+1):
    count = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and visited[i][j] == 0:
                visited[i][j] = 1
                find_area(i, j, height)
                count += 1
    # print(visited)
    answer.append(count)

print(max(answer))
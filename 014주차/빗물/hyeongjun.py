# 백준 14719 파이썬

# 블록이 쌓이면 블록 사이에 빗물이 고인다.
# 고이는 빗물의 총량은?

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))

# 왼쪽 오른쪽에 벽이 없고 맵 밖으로 나가면 빗물 못모음

# 오른쪽으로 90도 돌린 배열
world = [[0] * h for _ in range(w)]

for i in range(w):
    for j in range(arr[i]):
        world[i][j] = 1     # 블록을 1로 표시

answer = 0
for i in range(h):
    flag = False # 블록을 만나기 전
    count = 0
    for j in range(w):
        if not flag and world[j][i] == 1:
            flag = True
            

        elif flag and world[j][i] == 0:
            count += 1

        elif flag and world[j][i] == 1:
            answer += count
            count = 0
                    
print(answer)
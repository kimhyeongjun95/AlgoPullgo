# 백준 14503 로봇 청소기

# 장소 : N x M
# 1. 현재 위치 청소
# 2. 왼쪽 방향부터 인접 칸 탐색
# 2-0. 왼쪽 청소 not done -> 회전 and 전진
# 2-1. 청소할 공간이 없다면 그 방향으로 회전, 2번으로 돌아가기
# 2-2. 네 방향 이미 청소가 되어있구나 벽인 경우, 바라보는 방향을 유지한 채로 한칸 후진 -> 2번
# 2-3. 청소 and 벽 and 뒤쪽도 벽이라 후진 불가능이면 stop

# 로봇 청소기가 청소하는 칸의 개수 출력

import sys
input = sys.stdin.readline

# 1. 현재 위치에서 함수 시작하기
# 2. 보는 방향에 따른 델타값 만들기
# 3. 네방향 청소 -> 예외문 만들어서 후진하기
# 4. 마지막 예외문 처리

# 북 동 남 서
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def robot(x, y, direction):
    stack = [(x, y)]
    answer = 0
    while stack:
        x, y = stack.pop()

        # 청소한 구역 2로 표시
        if arr[x][y] == 0:
            arr[x][y] = 2
            answer += 1
        
        # 왼쪽 바라보고 이동하기
        for i in range(4):
            direction = (direction - 1) % 4

            # for dx, dy in dxy[direction]:
            nx = x + dxy[direction][0]
            ny = y + dxy[direction][1]
            if -1 < nx < n and -1 < ny < m:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    break

        # 4방향 다 막혔을 경우 후진
        else:
            nx = x - dxy[direction][0]
            ny = y - dxy[direction][1]
            if -1 < nx < n and -1 < ny < m:
                # 뒤쪽 방향도 벽이라 후진 x -> 작동 멈춤
                if arr[nx][ny] == 1:
                    return answer
                # 청소한 구역(후진 가능)
                elif arr[nx][ny] == 2:
                    stack.append((nx, ny))
    
    return answer

n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = robot(x, y, d)
print(answer)

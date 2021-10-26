# 백준 3190 뱀


# 사과를 먹으면 뱀 길이가 늘어남
# 벽 또는 자기자신의 몸과 부딪히면 게임이 끝남

# N x N, 몇몇 칸에는 사과
# 처음 뱀의 길이는 1, 처음에는 오른쪽을 향함

# 매 초 몸길이를 늘려 머리를 다음칸에 위치
# 사과 O -> 사과 x and 꼬리 not move
# 사과 X -> 몸 길이 변화 X 꼬리 move

# 
# 몇초에 게임이 끝날까?
import sys
input = sys.stdin.readline
from collections import deque

#    우/하/좌/상 -> 숫자 증가 : 오른쪽 턴
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snake():
    count = 0
    
    # 뱀 꼬리 위치
    # 꼬리를 큐로 저장해 저장한 순서대로 tail 위치가 변할 수 있도록..
    tail = deque([(0, 0)])
    nx, ny = 0, 0
    direction = 0 # 처음엔 오른쪽으로 간다.
    while True:
        # 뱀이 방향 바꿀 시간이라면
        if time:
            if count == int(time[0][0]):
                t, d = time.popleft()
                if d == 'L': # 왼
                    direction = (direction-1)%4
                elif d == 'D': # 오
                    direction = (direction+1)%4

        nx = dx[direction] + nx
        ny = dy[direction] + ny
        # 벽을 만나면 종료
        count += 1

        if 0 > nx or n <= nx or 0 > ny or n <= ny:
            return count
        # 자기 자신을 만나면 종료
        if board[nx][ny] == 1:
            return count

        # 사과를 못만나면
        elif board[nx][ny] == 0:
            x, y = tail.popleft()
            board[x][y] = 0 # 꼬리제거
        
        board[nx][ny] = 1 # 만나던지 못만나던지 계속 이동
        tail.append((nx, ny)) # 꼬리위치 갱신


n = int(input()) # 보드의 크기
k = int(input()) # 사과
board = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2 # 사과는 2로 표시
board[0][0] = 1 # 뱀의 꼬리 1로 표시
# 즉, 0:통로 1:꼬리 2:사과

l = int(input()) # 뱀 move
time = deque([])
for _ in range(l):
    t, direction = input().split() # L: 왼쪽, D: 오른쪽
    time.append((t, direction))

answer = snake()

print(answer)
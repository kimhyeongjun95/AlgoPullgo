# 백준 21610 마법사 상어와 비바라기

# 파이어볼 토네이도 파이어스톰 물복사버그
# 비바라기 -> 하늘에 비구름

# N x N
# 칸 마다 바구니, 저장할 수 있는 물의 양 제한 x
# 1번과 N번 연결
# (N, 1), (N, 2), (N-1, 1), (N-1, 2) -> 즉 2x2
# M번 명령, 8개의 방향

# 이동을 명령하면
# 1. 모든 구름이 이동
# 2. 각 구름에서 비가 내려 칸의 바구니 물 += 1
# 3. 구름이 모두 사라짐
# 4. 2에서 물이 증가한 칸에 물 복사버그 마법 시전
#       대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼 바구니의 물이 양이 증가
#       ex) (N, 2) 인접 칸은 (N-1, 1), (N-1, 3)
#       ex) (N, N)은 (N-1, N-1)
# 5. 저장된 물의 양이 2 이상인 모든칸에 구름 생성 -> 물의 양 -= 2
#    구름이 생기는 칸은 3에서 사라진 칸이 아니어야한다.

# 남은 바구니의 물의 합


from collections import deque
from collections import defaultdict
# 1~8 왼쪽부터 시계방향
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dxy = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
orders = [list(map(int, input().split())) for _ in range(m)]
stack = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

for order in orders:
    cx, cy = order[0]-1, order[1]

    # 중복 체크용
    check = defaultdict(list)

    for _ in range(len(stack)):
        x, y = stack.popleft()
        dx = dxy[cx][0]
        dy = dxy[cx][1]
        nx = (x + (dx * cy)) % n
        ny = (y + (dy * cy)) % n
        stack.append((nx, ny))
        check[(nx, ny)] = 1

    for i in range(len(stack)):
        arr[stack[i][0]][stack[i][1]] += 1
    
    while stack:
        x, y = stack.popleft()
        count = 0
        # 대각선 확인
        for i in range(1, len(dxy), 2):
            dx = dxy[i][0]
            dy = dxy[i][1]
            nx = x + dx
            ny = y + dy
            if -1 < nx < n and -1 < ny < n:
                if arr[nx][ny] > 0:
                    count += 1
        
        arr[x][y] += count
        
    # stack 빈 상태
    # 구름 생성
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not check[(i, j)]:
                stack.append((i, j))
                arr[i][j] -= 2

answer = 0
for i in range(n):
    for j in range(n):
        answer += arr[i][j]

print(answer)
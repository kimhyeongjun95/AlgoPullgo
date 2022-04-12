# 백준 2638 치즈

# N x M 모눈종이
# 치즈가 표시

# 4변 중 2변 이상이 외부공기와 접촉 -> 한시간 만에 녹음

# 모든 치즈가 녹는데 걸리는 시간은?

# 0 공백 1 치즈

# 1. 매번 외각 치즈 찾기
#   1-1. 바깥 공기 dfs로 표시
#   1-2. 바깥 공기 확인
# 2. 외각 치즈 없애기
# 3. 시간 += 1
# 4. 1에서 못찾으면 시간출력

dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def outair(arr):
    # 1-1
    stack = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                stack.append((i, j))
                return stack

def outer(arr):
    # 차라리 그냥 0,0으로 시작했으면 됐을듯?
    stack = outair(arr)
    while stack:
        x, y = stack.pop()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if -1 < nx < n and -1 < ny < m and not arr[nx][ny]:
                # 바깥 공기 2 표시
                arr[nx][ny] = 2
                stack.append((nx, ny))

    result = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                count = 0
                for dx, dy in dxy:
                    nx = i + dx
                    ny = j + dy
                    # 1-2
                    if arr[nx][ny] == 2:
                        count += 1
                    if count >= 2:
                        result.append((i, j))
                        break
    return result

def remove_cheese(waiting):
    # 2
    for i, j in waiting:
        arr[i][j] = 0

    # 1-2
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                arr[i][j] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0

while True:
    # 1
    result = outer(arr)
    # 4
    if not result:
        break
    # 2
    remove_cheese(result)
    # 3
    time += 1

print(time)
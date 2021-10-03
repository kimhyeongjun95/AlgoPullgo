def safe_area(arr, high):
    new_arr = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # high보다 크거나 같으면 물에 잠기지 않음(0), 아니면 잠김(1)
            if arr[i][j] < high:
                new_arr[i][j] = 1
    
    return new_arr


def bfs(i, j):
    queue = [(i, j)]
    new_arr[i][j] = 1

    dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    while queue:
        x, y = queue.pop(0)

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if nx in range(N) and ny in range(N) and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 1
                queue.append((nx,ny))


N = int(input())

arr = []
min_num = 100
max_num = 1

for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

    if min(temp) < min_num:
        min_num = min(temp)
    elif max(temp) > max_num:
        max_num = max(temp)

max_cnt = 0
for high in range(min_num, max_num+1):
    new_arr = safe_area(arr, high)

    cnt = 0
    
    i = 0
    while i < N:
        j = 0
        while j < N:
            if new_arr[i][j] == 0:
                bfs(i, j)
                cnt += 1

            j += 1
        i += 1
    
    if cnt > max_cnt:
        max_cnt = cnt
    
print(max_cnt)
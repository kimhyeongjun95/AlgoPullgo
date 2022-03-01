N = int(input())
like = {}
for _ in range(N**2):
    lst = list(map(int, input().split()))
    like[lst[0]] = lst[1:]

room = [[0 for _ in range(N)] for _ in range(N)]
dxy = [(1,0),(-1,0),(0,1),(0,-1)]

for key in like:
    priority = []
    for x in range(N):
        for y in range(N):
            like_cnt, empty_cnt = 0, 0
            if not room[x][y]:
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not room[nx][ny]:
                            empty_cnt += 1
                        elif room[nx][ny] in like[key]:
                            like_cnt += 1
                priority.append((like_cnt, empty_cnt, x, y))
    priority.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    room[priority[0][2]][priority[0][3]] = key

answer = 0
for x in range(N):
    for y in range(N):
        like_cnt = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] in like[room[x][y]]:
                    like_cnt += 1
        if like_cnt:
            answer += 10**(like_cnt-1)
print(answer)
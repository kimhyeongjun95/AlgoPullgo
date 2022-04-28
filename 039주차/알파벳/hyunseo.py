# 백준 1987 알파벳

def dfs(x, y, cnt):
    global answer

    answer = max(answer, cnt)

    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        
        if 0 <= nx < R and 0 <= ny < C and not used[ord(alphabet[nx][ny])-65]:
            used[ord(alphabet[nx][ny])-65] = 1
            dfs(nx, ny, cnt+1)
            used[ord(alphabet[nx][ny])-65] = 0


R, C = map(int, input().split())
alphabet = [list(input()) for _ in range(R)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

used = [0 for _ in range(26)]
used[ord(alphabet[0][0])-65] = 1

answer = 0
dfs(0, 0, 1)

print(answer)
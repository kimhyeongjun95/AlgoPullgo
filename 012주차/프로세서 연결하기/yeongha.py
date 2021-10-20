def length_wire(cores):
    total = 0
    for core in cores:  # left, up, right, down
        if core[2] == 0:
            total += core[1]
        elif core[2] == 1:
            total += core[0]
        elif core[2] == 2:
            total += N-core[1]-1
        elif core[2] == 3:
            total += N-core[0]-1
    return total

def dfs(n, cnt):
    global ans, ans_total
    if cnt + cores_cnt-n < ans:  # 가지치기
        return
    if n >= cores_cnt:  # 베이스 라인
        if cnt > ans:
            ans = cnt
            ans_total = length_wire(cores)
        elif cnt == ans:
            total = length_wire(cores)
            if total < ans_total:
                ans_total = total
        return

    x, y, z = cores[n]
    if cores[n][2] == 5:
        dfs(n+1, cnt+1)
    else:
        dfs(n+1, cnt)
        d = [1]*4  # left, up, right, down
        for m in range(0, n):    
            if x == cores[m][0]:
                d[0] = 0
            elif y == cores[m][1]:
                d[1] = 0
            elif x > cores[m][0] and y > cores[m][1]:
                if cores[m][2] == 2:
                    d[1] = 0
                elif cores[m][2] == 3:
                    d[0] = 0
            elif x > cores[m][0] and y < cores[m][1]:
                if cores[m][2] == 0:
                    d[1] = 0
                elif cores[m][2] == 3:
                    d[2] = 0
                
        for m in range(n+1, cores_cnt):
            if x == cores[m][0]:
                d[2] = 0
            elif y == cores[m][1]:
                d[3] = 0
        
        for i in range(4):
            if d[i] == 1:
                cores[n][2] = i
                dfs(n+1, cnt+1)
                cores[n][2] = -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    cores.append([i,j,5])
                else:
                    cores.append([i,j,-1])
        
    cores_cnt = len(cores)
    ans = ans_total = 0
    dfs(0, 0)
    print('#{} {}'.format(tc, ans_total))
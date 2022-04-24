# 백준 4485 녹색 옷 입은 애가 젤다지?

import sys, heapq

def dijkstra():
    global amount

    heap = []
    heapq.heappush(heap, (amount[0][0], 0, 0))
    
    while heap:
        min_val, x, y = heapq.heappop(heap)

        if x == N-1 and y == N-1:
            return
            
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy

            if 0 <= nx < N and 0 <= ny < N and amount[nx][ny] > min_val + cave[nx][ny]:
                amount[nx][ny] = min_val + cave[nx][ny]
                heapq.heappush(heap, (amount[nx][ny], nx, ny))


input = sys.stdin.readline

i = 1
while True:
    N = int(input())

    if not N:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    amount = [[float('inf') for _ in range(N)] for _ in range(N)]
    amount[0][0] = cave[0][0]

    dijkstra()

    print(f'Problem {i}: {amount[N-1][N-1]}')
    i += 1
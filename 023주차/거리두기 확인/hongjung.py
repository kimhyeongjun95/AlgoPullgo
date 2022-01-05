from collections import deque

def solution(places):
    def bfs(i, j, list1):
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        visited = [[False] * 5 for _ in range(5)]
        visited[i][j] = True
        queue = deque([[i, j, 0]])
        while queue:
            ti, tj, distance = queue.popleft()
            if distance >= 2:
                continue
            for d in range(4):
                ni = ti + di[d]
                nj = tj + dj[d]
                if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj] == False:
                    if list1[ni][nj] == 'O':
                        queue.append([ni, nj, distance + 1])
                        visited[ni][nj] = True
                    elif list1[ni][nj] == 'X':
                        queue.append([ni, nj, distance + 2])
                        visited[ni][nj] = True
                    else:
                        if distance + 1 <= 2:
                            return 0
        return 1

    answer = []
    for place in places:
        p_positions = []
        cnt = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_positions.append([i, j])
                    cnt += 1
        
        result = 0
        for p in p_positions:
            if bfs(p[0], p[1], place):
                result += 1
            else:
                break
        if cnt == result:
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
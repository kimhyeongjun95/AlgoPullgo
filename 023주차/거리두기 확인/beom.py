from collections import deque

def bfs(p):
    start = []

    # 시작점이 되는 P 좌표 구하기
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0]*5 for i in range(5)]   # 방문 처리 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1
        
        while queue:
            y, x = queue.popleft()
        
            dx = [-1, 1, 0, 0] 
            dy = [0, 0, -1, 1]  

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:
                    
                    # 'O'의 자리를 다시 시작점으로 설정
                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    #  'P'이고 시작점부터의 거리가 1보다 작거나 같을 경우
                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for i in places:
        answer.append(bfs(i))
    
    return answer
# 프로그래머스 거리두기 확인하기

from collections import deque

def solution(places):
    def is_right(place):
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
        
        dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for person in people:
            first_x, first_y = person[0], person[1]
            
            queue = deque()
            queue.append((first_x, first_y, 0))
            
            visited = [[0 for _ in range(5)] for _ in range(5)]
            visited[first_x][first_y] = 1
            
            while queue:
                x, y, dist = queue.popleft()

                if dist >= 2:
                    continue

                for dx, dy in dxy:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        
                        if place[nx][ny] == 'O':
                            queue.append((nx, ny, abs(first_x-nx)+abs(first_y-ny)))
                        elif place[nx][ny] == 'P':
                            return False
        
        return True
        
    answer = []
    for place in places:
        if is_right(place):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer
# 프로그래머스 거리두기 확인하기
# 거리두기 O: 1, X: 0

# 5x5가 5개 들어오고
# 원소 5개 리스트 return
# 거리두기 : 3 이상

# P 응시자
# O 빈 테이블
# X 파티션
dxy = [(0,1), (0, -1), (1, 0), (-1, 0)]
def check(places, i, j, k):
    stack = []
    x = j
    y = k
    stack = [(x, y, 3)]
    visited = [[0] * 5 for _ in range(5)]
    visited[j][k] = 1
    while stack:
        x, y, count = stack.pop()
        
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            nc = count - 1
            if nc == 0:
                break
            if -1 < nx < 5 and -1 < ny < 5:
                if not visited[nx][ny]:
                    if places[i][nx][ny] == 'O':
                        visited[nx][ny] = 1
                        stack.append((nx, ny, nc))
                    elif places[i][nx][ny] == 'P' and nc > 0:
                        return False

    return True
        

def solution(places):
    answer = []
    for i in range(len(places)):
        dist = True
        for j in range(len(places)):
            if not dist:
                break
            for k in range(len(places)):
                if places[i][j][k] == 'P':
                    if not check(places, i, j, k):
                        dist = False
                        break
        if not dist:
            answer.append(0)
        else:
            answer.append(1)
    return answer
            
        
print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])) 
# [1, 0, 1, 1, 1]
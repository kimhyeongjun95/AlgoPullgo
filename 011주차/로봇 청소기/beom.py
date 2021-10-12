import sys
input = sys.stdin.readline


def turn(d):
    if d == 0:
        return 3
    else:
        return d-1


def robot(y, x, d, cnt):
    while True:
        # 사방이 막혔으므로 후진
        if cnt == 4:
            back_x = x + dx[(d+2)%4]
            back_y = y + dy[(d+2)%4]
            
            # 후진하는 방향이 청소했으면 후진하면서 변수 갱신
            if area[back_y][back_x] == -1:
                y, x, d, cnt = back_y, back_x, d, 0
            
            # 그게 아니라면 청소한 구역의 개수 리턴
            else:
                result = 0
                for i in range(N):
                    for j in range(M):
                        if area[i][j] == -1:
                            result += 1

                return result
        
        # 청소안했으면 청소
        if area[y][x] == 0:
            area[y][x] = -1
        
        # 방향을 왼쪽으로 바꾼다.
        turn_d = turn(d)
        turn_x = x + dx[turn_d]
        turn_y = y + dy[turn_d]

        # 좌표를 저장하고, 청소를 안했으면 회전한 곳으로 갱신
        if area[turn_y][turn_x] == 0:
            y, x, d, cnt = turn_y, turn_x, turn_d, 0
        # 그게 아니라면(청소했거나, 막혔거나)
        else:
            y, x, d, cnt = y, x, turn_d, cnt+1
            

N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

print(robot(r, c, d, 0))
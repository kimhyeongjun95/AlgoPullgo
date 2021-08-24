import sys

N = int(sys.stdin.readline())

city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 도시의 모드 높이 리스트로 입력받기
max_h = 0 # 최고 높이 변수
for i in range(N): # 최고 높이 구하는 과정
    for j in range(N):
        if city[i][j] > max_h:
            max_h = city[i][j]

result = [] # '1'부터 '최고 높이-1'까지의 안전 영역 모두 result에 추가
for H in range(1, max_h): # 장마철 높이를 하나씩 증가시키면서 반복
    city_check = [[0] * N for _ in range(N)] # 침수 여부 확인을 위한 빈 리스트 생성
    for i in range(N):
        for j in range(N):
            if city[i][j] <= H: # 만약 침수되었다면 해당 인덱스를 1로 변환
                city_check[i][j] = 1

    di = [-1, 1, 0, 0] # 상 하 좌 우
    dj = [0, 0, -1, 1]
    safe = 0 # 안전지역 개수
    for i in range(N):
        for j in range(N):
            if city_check[i][j] == 0:
                safe += 1 # 만약 해당 인덱스가 0이면 이제 안전지역 1곳 추가
                city_check[i][j] = 1 # 지금 위치를 1로 변환하고
                stack = [[i, j]] # 스택에 추가
                ni = i # 현재 위치
                nj = j
                while True:
                    mi = ni # 현재 위치
                    mj = nj
                    for d in range(4):
                        ni = mi + di[d] # 이동 위치
                        nj = mj + dj[d]
                        if 0 <= ni <= N - 1 and 0 <= nj <= N - 1: # 이동 위치가 범위 안이고
                            if city_check[ni][nj] == 0: # 그 이동 위치가 침수가 되어있지 않은 지역이라면
                                city_check[ni][nj] = 1 # 그 위치도 1로 변환
                                stack.append([ni, nj]) # 스택에 그 위치 인덱스 추가
                                break
                    else: # 만약 현재 위치에서 갈 수 있는 모든 이동 위치가 침수지역이라면
                        stack.pop() # 스택에서 pop
                        if len(stack) == 0: # 만약 스택이 비어있다면 이 지역에서 침수가 되지 않은 지역 모두 체크 완료!
                            break
                        ni = stack[-1][0] # 스택의 마지막 인덱스로 현재 위치 변환
                        nj = stack[-1][1]

    result.append(safe) # 안전지역 개수를 결과값에 추가

if result == []: # 도시의 모든 높이가 똑같다면 0이 되므로 이때의 최대 안전지역 개수인 1을 출력
    print(1)
else:
    print(max(result)) # 가장 큰 개수를 출력
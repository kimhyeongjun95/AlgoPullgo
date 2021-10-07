# 백준 12865 평범한 배낭 : knapsack algorithm

import sys

N, K = map(int, sys.stdin.readline().split())

# 가로축 : 무게 (0~K) / 세로축 : 개수 (0~N)
# 그 전값과 비교할 때 첫 번째 값도 비교를 해주기 위해서 0번 인덱스도 생성
bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
things = [[0, 0]]  # (무게, 가치)

for _ in range(N):
    things.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = things[i][0]
        value = things[i][1]

        if j < weight:
            # 물건을 가방에 넣어줄 수 없음 
            # -> 물건을 가방에 넣기 바로 이전의 상태 그대로 가져오기
            bag[i][j] = bag[i-1][j]
        else:
            # 물건을 가방에 넣어줄 수 있음
            # -> 물건을 가방에 넣은 전/후의 가치를 비교해서 더 큰 가치값으로 채우기
            before = bag[i-1][j]
            after = value + bag[i-1][j-weight]

            bag[i][j] = max(before, after)

print(bag[N][K])
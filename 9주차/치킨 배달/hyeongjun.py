# 백준 15686 치킨 배달

# N x N 도시
# 2차원행렬 r과 c, 1부터 시작
# -> i와 j에 1씩 더해주면 될거같다. 

# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 = sum(치킨거리)

# 0: 빈칸, 1: 집, 2: 치킨집

# m개의 치킨집을 고르고,
# 도시의 치킨거리의 최솟값 출력

# 치킨거리 : |r1-r2| + |c1-c2|

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 경우의 수를 다 계산하는게 최선인거 같다

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1: #집 
            house.append((i, j))
        if city[i][j] == 2: #치킨집
            chicken.append((i, j))

combo = list(combinations(chicken, m))
# for i in combo:
#     print(i)

answer = [0] * len(combo)
for i in house: # 집 순회
    for j in range(len(combo)):
        result = n**2
        for k in combo[j]:
            temp = abs(i[0]-k[0]) + abs(i[1]-k[1])
            result = min(result, temp) # 가까운 치킨집 구하기
      
        # 매번 다른 집의 위치마다
        # 이 치킨집의 경우의 수에 해당하는 인덱스에 더해준다.
        answer[j] += result 
print(min(answer))
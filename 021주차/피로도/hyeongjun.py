# 프로그래머스 피로도
# 최소 필요 피로도 : 탐험을 시작하기 위해 필요한 
# 소모 피로도 : 던전 탐험을 마쳤을때 소모되는

# 순열

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for per in list(permutations(dungeons, len(dungeons))):
        count = 0
        energy = k
        for least, cost in per:
            if energy < least:
                break
            energy -= cost
            count += 1
        answer = max(answer, count)
    return answer
print(solution(80, [[80,20],[50,40],[30,10]])) # 3
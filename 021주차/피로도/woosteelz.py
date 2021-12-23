from itertools import permutations


def get_max(k, dungeon):
    cnt = 0
    for require, cost in dungeon:
        if require <= k:
            cnt += 1
            k -= cost
    return cnt


def solution(k, dungeons):
    answer = -1
    for dungeon in list(permutations(dungeons, len(dungeons))):
        answer = max(answer, get_max(k, dungeon))
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))

from itertools import permutations

def solution(k, dungeons):
    def game(n, p):
        nonlocal ans, lst

        if n > ans:
            ans = n

        if n == C:
            return

        if p >= lst[n][0]:
            game(n+1, p - lst[n][1])
        
    ans = 0
    C = len(dungeons)
    for lst in permutations(dungeons, C):
        game(0, k)

    return ans
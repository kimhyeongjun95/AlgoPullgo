from collections import defaultdict

def solution(n, results):
    def dfs(a):
        nonlocal matches, results_dict

        stack = [a]
        while stack:
            winner = stack.pop()
            for loser in results_dict[winner]:
                if matches[a][loser] == 0:
                    matches[a][loser] = 1
                    matches[loser][a] = 2
                    stack.append(loser)

    answer = 0
    matches = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        matches[i][i] = 3

    results_dict = defaultdict(list)
    for a, b in results:
        results_dict[a].append(b)
    
    for i in range(1, n + 1):
        dfs(i)

    answer = 0
    for i in range(1, n + 1):
        if 0 not in matches[i][1:]:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
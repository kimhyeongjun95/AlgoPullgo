def solution(begin, target, words):
    def dfs(current, idx):
        nonlocal answer, length1, length2
        if current == target:
            if answer > sum(visited):
                answer = sum(visited)
            return
        
        if idx == len(words):
            return
        
        for i in range(length1):
            if visited[i] == 0:
                cnt = 0
                for j in range(length2):
                    if words[i][j] != current[j]:
                        cnt += 1
                if cnt == 1:
                    visited[i] = 1
                    dfs(words[i], idx + 1)
                    visited[i] = 0

    if target not in words:
        return 0
    length1 = len(words)
    length2 = len(begin)
    answer = float('inf')
    visited = [0] * len(words)
    dfs(begin, 0)
    if answer == float('inf'):
        return 0
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
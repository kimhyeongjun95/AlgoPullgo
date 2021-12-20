def solution(begin, target, words):
    def dfs(word, n):
        nonlocal answer

        if n >= answer:
            return
        
        if word == target:
            answer = min(answer, n)

        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for a,b in zip(word, words[i]):
                    if a != b:
                        cnt += 1
                        if cnt > 1:
                            break
                else:
                    visited[i] = 1
                    dfs(words[i], n+1)
                    visited[i] = 0

    answer = float('inf')
    if target not in words:
        return 0

    visited = [0] * len(words)
    dfs(begin, 0)

    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))

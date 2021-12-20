# 프로그래머스 단어 변환

def solution(begin, target, words):
    if target not in words:
        return 0
    
    stack = [(begin, 0)]
    visited = [0 for _ in range(len(words))]
    N = len(begin)
    
    while stack:
        word, cnt = stack.pop()
        if word == target:
            return cnt
        
        for i in range(len(words)):
            if not visited[i]:
                c = 0
                for j in range(N):
                    if word[j] != words[i][j]:
                        c += 1
                
                if c == 1:
                    visited[i] = 1
                    stack.append((words[i], cnt+1))
# 프로그래머스 단어 변환
# begin -> target 변환 과정
# hit -> hot -> dot -> dog -> cog # 4단계

# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 단어의 길이는 모두 같음

def check(begin, word):
    count = 0
    for b, w in zip(begin, word):
        if b!= w:
            count += 1
    # 알파벳 하나만 다르면 True 아니면 False
    return count == 1


def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = [0] * len(words)
    stack = [begin]
    while stack:
        popped = stack.pop()
        if popped == target:
            return answer
        
        for i in range(len(words)):
            # 방문 안했으면
            if not visited[i]:
                # 알파벳 하나만 다르면
                if check(popped, words[i]):
                    # 방문처리
                    visited[i] = 1
                    stack.append(words[i])
        answer += 1
    return answer

print(solution("hit", "cog", 
["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", 
["hot", "dot", "dog", "lot", "log"])) # 0

# 프로그래머스 피로도

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for perm in permutations(dungeons, len(dungeons)):
        stack = list(perm)
        hp = k
        cnt = 0
        
        while stack:
            need, use = stack.pop()
            
            if hp >= need:
                hp -= use
                cnt += 1
        
        answer = max(answer, cnt)
        
    return answer

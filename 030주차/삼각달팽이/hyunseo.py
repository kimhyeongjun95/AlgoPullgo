# 프로그래머스 삼각 달팽이

def solution(n):
    snail = [[0 for _ in range(i+1)] for i in range(n)]
    
    num = 0
    i = -1
    j = 0
    
    for m in range(n):
        for _ in range(m, n):
            if m%3 == 0: #아래
                i += 1
            elif m%3 == 1: # 왼쪽
                j += 1
            else: # 위
                i -= 1
                j -= 1
                
            num += 1
            snail[i][j] = num
    
    answer = []
    
    for row in snail:
        answer += row
            
    return answer
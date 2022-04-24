# 프로그래머스 숫자게임

def solution(A, B):
    A.sort()
    B.sort()
    
    i = 0
    j = 0
    answer = 0
    
    while i < len(A) and j < len(B):
        while A[i] >= B[j]:
            j += 1
            
            if j == len(B):
                return answer
        
        answer += 1
        i += 1
        j += 1
        
    return answer


print(solution([5,1,3,7], [2,2,6,8]))
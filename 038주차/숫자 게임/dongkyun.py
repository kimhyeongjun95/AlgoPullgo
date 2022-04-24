def solution(A, B):
    answer = 0
    N = len(A)
    i = 0
    flag = False
    
    for y in range(N):
        bub = 0
        max_dep = 873981279879123
        for x in range(i,N):
            if i == N-1:
                flag = True
                break
            if A[y] < B[x]:
                if max_dep > B[x]-A[y]:
                    max_dep = B[x]-A[y]
                    bub = x
        if flag:
            break
        B[bub], B[y] = B[y], B[bub]
        i += 1
        print(B)
    for a in range(N):
        if A[a] < B[a]:
            answer +=1
            
    return answer
import sys

A, B = sys.stdin.readline().rstrip().split()

min_cnt = len(B)

for n in range(len(B)-len(A)+1) :
    
    cnt = 0
    for i in range(len(A)) :
        if A[i] != B[n:][i] :
            cnt += 1

    if cnt < min_cnt :
        min_cnt = cnt

print(min_cnt)
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

answer = [-1]*N
stack = []
idx_stack = []

i = 0

while i < N:
    if stack and stack[-1] < A[i]:
        stack.pop()
        answer[idx_stack.pop()] = A[i]
        continue
    else:
        stack.append(A[i])
        idx_stack.append(i)
    
    i += 1

print(*answer)
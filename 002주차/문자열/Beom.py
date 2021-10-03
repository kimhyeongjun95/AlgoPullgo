A, B = input().split()
B = list(B)
max_count = 0

while len(A) <= len(B):
    count = 0
    
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
    max_count = max(max_count, count)
    B.pop(0)
    
print(len(A)-max_count)
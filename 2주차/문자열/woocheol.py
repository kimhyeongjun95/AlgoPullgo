A, B = input().split()

ans = []

for i in range(len(B) - len(A) + 1):
    cnt = 0
    k = 0
    while k < len(A):
        if not A[k] == B[k + i]:
            cnt += 1
        k += 1
    ans.append(cnt)
print(min(ans))

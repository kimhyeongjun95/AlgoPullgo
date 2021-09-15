# 2960번 에라토스테네스의 체
n, k = map(int, input().split())
prime = [False for _ in range(n+1)]
ans = 0
for i in range(2, n+1):
    temp = i
    while temp < n+1:
        if prime[temp] == False:
            prime[temp] = True
            k -= 1
            if not k:
                ans = temp
                break
        temp += i
    if ans:
        break

print(ans)

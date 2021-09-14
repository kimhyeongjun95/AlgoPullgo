import sys

N, K = map(int, sys.stdin.readline().split())

numbers = list(range(2, N+1))

cnt = 0
result = 0
flag = False
while numbers:
    P = numbers.pop(0)
    cnt += 1
    if cnt == K:
        result = P
        break
    i = 2
    while P * i <= N:
        if P * i in numbers:
            numbers.remove(P*i)
            cnt += 1
            if cnt == K:
                result = P * i
                flag = True
                break
        i += 1
    if flag:
        break

print(result)
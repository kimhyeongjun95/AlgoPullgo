import sys
N = int(sys.stdin.readline())

money = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        money.pop()
    else:
        money.append(n)
print(sum(money))
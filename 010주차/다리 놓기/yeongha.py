def calc(n,m):
    global ans
    if n == 0:
        return
    ans = ans*m/n
    calc(n-1, m-1)

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    ans = 1
    calc(N,M)
    print(round(ans))

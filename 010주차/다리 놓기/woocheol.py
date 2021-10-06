from math import factorial

for _ in range(int(input())):
    n, m = map(int, input().split())
    # mCn
    ans = factorial(m) // (factorial(n) * factorial(m-n))
    print(ans)

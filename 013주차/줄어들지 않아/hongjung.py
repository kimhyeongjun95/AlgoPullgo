import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    result = defaultdict()
    if n == 1:
        print(10)
    else:
        result[1] = [1] * 10
        start = 10
        for i in range(2, n+1):
            result[i] = [start] + [0] * 9
            for j in range(1, 10):
                result[i][j] = result[i][j-1] - result[i-1][j-1]
            start = sum(result[i])

        print(sum(result[n]))

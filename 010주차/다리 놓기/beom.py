import sys
input = sys.stdin.readline
import math

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    answer = math.factorial(M) // (math.factorial(M - N) * math.factorial(N))
    print(answer)
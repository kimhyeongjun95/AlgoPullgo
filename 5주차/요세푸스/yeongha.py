# 요세푸스 문제
import sys
from collections import deque

def Josephus(N, K):
    result = []
    i = 0
    while peoples:
        i += 1
        people = peoples.popleft()
        if i % K :
            peoples.append(people)
        else:
            result.append(people)
    return result

N, K = map(int,sys.stdin.readline().split())
peoples = deque([i for i in range(1, N+1)])
print('<'+", ".join(list(map(str, Josephus(N, K))))+'>')


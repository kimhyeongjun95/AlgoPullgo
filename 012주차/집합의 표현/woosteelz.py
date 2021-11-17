# 1717 집합의 표현
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(n + 1)]


def find(num):
    if num == arr[num]:
        return num
    temp = find(arr[num])
    arr[num] = temp
    return temp


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        arr[b] = a
    else:
        arr[a] = b


for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

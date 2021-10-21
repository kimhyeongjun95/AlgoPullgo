import sys

def make_one(n, cnt):
    global result
    if n == 1:
        if result > cnt:
            result = cnt
        return
    
    if cnt < result:
        if n % 3 == 0 and n//3 >= 1:
            make_one(n//3, cnt+1)
        if n % 2 == 0 and n//2 >= 1:
            make_one(n//2, cnt+1)
        if n - 1 >= 1:
            make_one(n-1, cnt+1)


N = int(sys.stdin.readline())

result = float('inf')
make_one(N, 0)

print(result)
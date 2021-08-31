import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

tx = t % (2*w)
ty = t % (2*h)

x = y = 1

curr = 0
while curr < tx:
    if p == 0 or p == w:
        x = -x

    p += x
    curr += 1

curr = 0
while curr < ty:
    if q == 0 or q == h:
        y = -y
    
    q += y
    curr += 1

print(p, q)
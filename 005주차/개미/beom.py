import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) // w
y = (q + t) // h

if x % 2:
    result_x = w - ((p + t) % w)
else:
    result_x = (p + t) % w

if y % 2:
    result_y = h - ((q + t) % h)
else:
    result_y = (q + t) % h

print(result_x, result_y)

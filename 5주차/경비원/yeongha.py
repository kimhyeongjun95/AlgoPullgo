# 경비원
def change(a):
    d, l = a[0], a[1]
    global W, H
    if d == 1:
        return l, 2*(H+W)-l
    elif d == 2:
        return 2*W+H-l, H+l
    elif d == 3:
        return 2*(W+H)-l, l
    else:
        return W+l, W+2*H-l

W, H = map(int, input().split())
N = int(input())
stores = [list(map(int, input().split())) for _ in range(N)]
d1, d2 = change(list(map(int, input().split())))

total = 0
for store in stores:
    s_d1, s_d2 = change(store)
    if d1 < s_d1:
        total += min(s_d1-d1, d1+s_d2)
    elif d1 > s_d1:
        total += min(d1-s_d1, s_d1+d2)
print(total)



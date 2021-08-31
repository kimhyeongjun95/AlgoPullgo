# 2564번 경비원
w, h = map(int, input().split())
num = int(input())
store = [list(map(int, input().split())) for _ in range(num)]
x, y = map(int, input().split())

ans = 0

for a, b in store:
    # north
    if x == 1:
        if a == 1:
            ans += abs(y - b)
        elif a == 2:
            ans += min(y + b, (w - y) + (w - b)) + h
        elif a == 3:
            ans += y + b
        elif a == 4:
            ans += (w - y) + b
    # south
    elif x == 2:
        if a == 1:
            ans += min(y + b, (w - y) + (w - b)) + h
        elif a == 2:
            ans += abs(y - b)
        elif a == 3:
            ans += y + (h - b)
        elif a == 4:
            ans += (w - y) + (h - b)
    # west
    elif x == 3:
        if a == 1:
            ans += y + b
        elif a == 2:
            ans += (h - y) + b
        elif a == 3:
            ans += abs(y - b)
        elif a == 4:
            ans += min(y + b, (h - y) + (h - b)) + w
    # east
    elif x == 4:
        if a == 1:
            ans += y + (w - b)
        elif a == 2:
            ans += (h - y) + (w - b)
        elif a == 3:
            ans += min(y + b, (h - y) + (h - b)) + w
        elif a == 4:
            ans += abs(y - b)
print(ans)

# def ant(w, h, x, y, t):
#     dx = [1, -1, -1, -1]
#     dy = [1, 1, -1, 1]

#     cnt = 0

#     i, j = x, y
#     k = 0
#     while cnt < t:
#         nx, ny = i+dx[k], j+dy[k]
#         if nx == x and ny == y and k == 0:
#             return 
#         if -1 < nx <= w and -1 < ny <= h:
#             cnt += 1
#             i, j = nx, ny
#         else:
#             k = (k+1) % 4
#     return [nx, ny]

w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

tx = t % (2*w)
ty = t % (2*h)

temp = True
for _ in range(tx):
    if x == w:
        temp = False
    elif x == 0:
        temp = True
    if temp: x += 1
    else: x -= 1

temp = True
for _ in range(ty):
    if y == h:
        temp = False
    elif y == 0:
        temp = True
    if temp: y += 1
    else: y -= 1

print(x, y)
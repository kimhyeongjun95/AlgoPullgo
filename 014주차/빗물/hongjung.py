import sys

H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

result = 0
while True:
    temp = 0
    add = False
    front_wall = False
    for i in range(W):
        if front_wall and blocks[i] == 0:
            temp += 1
        elif front_wall and blocks[i] > 0:
            blocks[i] -= 1
            result += temp
            add = True
            temp = 0
        elif not front_wall and blocks[i] > 0:
            blocks[i] -= 1
            front_wall = True
    
    if add == False:
        break

print(result)
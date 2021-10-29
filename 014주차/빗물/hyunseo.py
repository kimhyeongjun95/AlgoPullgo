# 백준 14719 빗물

def left(idx):
    global result

    if idx == 0:
        return
    
    temp = blocks[:idx]
    high = max(temp)
    for i in range(idx-1, -1, -1):
        if blocks[i] == high:
            for j in range(i+1, idx):
                result += high - blocks[j]
            left(i)
            return


def right(idx):
    global result

    if idx == W-1:
        return
    
    temp = blocks[idx+1:]
    high = max(temp)
    for i in range(idx+1, W):
        if blocks[i] == high:
            for j in range(idx+1, i):
                result += high - blocks[j]
            right(i)
            return


H, W = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0
for i in range(W):
    if blocks[i] == max(blocks):
        # 인덱스, 높이
        left(i)
        right(i)
        break

print(result)
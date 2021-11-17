# 14719번 빗물
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
temp = 0
max_idx = blocks.index(max(blocks))

for i in range(max_idx + 1):
    if temp < blocks[i]:
        temp = blocks[i]
    ans += temp

temp = 0
for i in range(W-1, max_idx, -1):
    if temp < blocks[i]:
        temp = blocks[i]
    ans += temp

print(ans-sum(blocks))

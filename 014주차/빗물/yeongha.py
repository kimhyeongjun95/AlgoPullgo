H, W = map(int, input().split())
blocks = list(map(int, input().split()))
start = 0
end = len(blocks)-1

while True:
    if blocks[start] > blocks[start+1]:
        break
    start += 1

while end:
    if blocks[end] > blocks[end-1]:
        break
    end -= 1

total = 0
for i in range(start+1, end):
    max_block = min(max(blocks[:i]), max(blocks[i+1:]))
    if blocks[i] < max_block:
        total += max_block - blocks[i]
print(total)
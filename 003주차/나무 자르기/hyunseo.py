import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

total = sum(trees)-M
trees.sort()

i = 0
while True:
    if trees[i] < total//N:
        total -= trees[i]
        N -= 1
    else:
        break

    i += 1

print(total//N)
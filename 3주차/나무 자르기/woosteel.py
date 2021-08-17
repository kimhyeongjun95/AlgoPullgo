# 2805번 나무 자르기

N, height = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
mid = 0
ans = []

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for tree in trees:
        temp += (tree - mid) if tree >= mid else 0

    if temp >= height:
        ans.append(mid)
        start = mid + 1
    elif temp < height:
        end = mid - 1
print(max(ans))

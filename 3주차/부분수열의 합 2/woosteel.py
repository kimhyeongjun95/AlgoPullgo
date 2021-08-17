# 1208번 부분수열의 합

num, total = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
# for i in range(1 << num):
#     temp = 0
#     for j in range(num):
#         if i & (1 << j):
#             temp += arr[j]
#     if temp == total:
#         ans += 1

# print(ans) if total else print(ans-1)

left = arr[:num//2]
right = arr[num//2:]
left_ans = []
right_ans = []

for i in range(1 << len(left)):
    temp = 0
    for j in range(len(left)):
        if i & (1 << j):
            temp += left[j]
    left_ans.append(temp)

for i in range(1 << len(right)):
    temp = 0
    for j in range(len(right)):
        if i & (1 << j):
            temp += right[j]
    right_ans.append(temp)

print(left_ans, right_ans)

ans = 0
for l in left_ans:
    for r in right_ans:
        if l + r == total:
            ans += 1

print(ans - 1)

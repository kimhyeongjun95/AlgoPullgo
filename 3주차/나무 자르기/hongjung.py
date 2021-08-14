# 1. 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

# start, end = 1, max(trees)

# while True:
#     middle = (start + end) // 2
#     tmp = 0
#     for tree in trees:
#         if tree - middle > 0:
#             tmp += (tree - middle)
#         if tmp > M:
#             break
#     if tmp == M:
#         break
#     elif tmp > M:
#         start = middle + 1
#     else:
#         end = middle - 1

# print(middle)


# 2. 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

# def cut(list1, h):
#     tmp = 0
#     for ele in list1:
#         if ele - h >= 0:
#             tmp += (ele - height)
#     return tmp
    

# height = max(trees)
# while True:
#     result = cut(trees, height)
#     if result == M:
#         break
#     height -= 1

# print(height)


# 3. 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

# height = max(trees)
# while True:
#     tmp = list(filter(lambda x: x > height, trees))
#     if sum(tmp) - len(tmp) * height == M:
#         break
#     height -= 1

# print(height)


# 4. 시간초과
# import sys

# N, M = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))

# height = max(trees)
# result = 0
# while True:
#     tmp = 0
#     for tree in trees:
#         remainder = tree - height
#         if remainder >= 0:
#             tmp += remainder
#     if tmp == M:
#         result = height
#         break
#     height -= 1

# print(result)
import sys

N = int(sys.stdin.readline())
numbers = [0] + list(map(int, sys.stdin.readline().split())) + [0]


# result = ''
# for i in range(1, N+1):
#     tmp = ''
#     for j in range(i+1, N+2):
#         if numbers[i] < numbers[j]:
#             tmp = str(numbers[j])
#             break
#     if tmp == '':
#         result += ('-1 ')
#     else:
#         result += (tmp + ' ')

# print(result)


# result = ''
# for i in range(1, N+1):
#     tmp = list(filter(lambda x: x > numbers[i], numbers[i+1:]))
#     if tmp == []:
#         result += '-1 '
#     else:
#         result += (str(tmp[0]) + ' ')

# print(result)


# i = 1
# j = 2
# result = ''
# while True:
#     if i == N:
#         result += '-1 '
#         break
#     if j == N + 1:
#         result += '-1 '
#         i += 1
#         j = i + 1
#     if numbers[j] > numbers[i]:
#         result += (str(numbers[j]) + ' ')
#         i += 1
#         j = i + 1
#     else:
#         j += 1

# print(result)

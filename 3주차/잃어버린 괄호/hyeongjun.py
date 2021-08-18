# 더하기 할때 괄호로치면? 되는거 같다.
# 숫자에만 괄호칠 수 있는듯, 곱하기로는 못 바꾸는거 같다.


# n = input()

# result = ''
# result_add = ''
# temp  = []
# temp_number = 0
# i = 0
# answer = 0

# while i < len(n):
#     if n[i] == '-': # 나중에 몰아서 빼주기
#         temp.append(int(result))
#         result = ''
#         i += 1

#     elif n[i] == '+':
#         while True:
#             if not n[i+1].isdigit:
#                 i += 1
#                 result_add += n[i]
#             temp_number += int(result) + int(result_add)
#             result = ''
#             result_add = ''

#     else: # 숫자일때
#         result += n[i]
#         i += 1

# answer = temp[0]
# for x in temp:
#     if x == temp[0]:
#         pass
#     answer -= x

# answer - temp_number

# print(answer)

# --------------------------------------------------------------------------

n = input()
# 마이너스로 가르고
s = n.split('-')

answer = [] # 다 마이너스할 리스트

for i in s:
    result = 0 # 더하기가 몇번 나올지 모르니
    temp = i.split('+')
    for x in temp:
        result += int(x)
    answer.append(result)

temp = answer[0] # 초기값 설정

for i in range(1, len(answer)):
    temp -= answer[i]

print(temp)
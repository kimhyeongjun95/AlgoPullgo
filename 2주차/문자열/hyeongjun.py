# 길이가 N으로 같은 문자열 X, Y
# 두 문자열의 차이는 X[i] != Y[i]인 i의 개수.
# X = 'jimin'
# Y = 'minji'
# 둘의 차이는 4 -> 2번째 i가 동일함. "i"

# len(a) <= len(b)
# 1. a 앞에 아무 알파벳 추가
# 2. a 뒤에 아무 알파벳 추가
# len(a) == len(b) and 차이를 최소화

# adaabc
# aababbc
# /aadaabc
# /aababbc
# 2 -> 앞에 추가, 이게 답
# /adaabcc
# /aababbc
# 3 -> 뒤에 추가, 차이가 더 큼

# aaaa
# bbbbaaaa
# /bbbbaaaa
# /bbbbaaaa
# 4번 추가를 했지만 차이는 0이다.
# /aaaaaaaa
# /bbbbaaaa
# 뒤에 추가를 하니 4차이가 4임

# aaa
# aaaabbbb 만약 이렇게 있다면

# aaa0000
# aaaabbb -> 차이는 0

# 0aaa000
# aaaabbb -> 차이는 0

# 00aaa00
# aaabbbb -> 차이는 2

# 처음에 이런 식으로 가장 차이가 적은 것을 찾으면 되겠다.

import sys

a, b = sys.stdin.readline().split()
count_list = []


for i in range(len(b) - len(a)+1): # 차이만큼 반복 할 수 있도록 # +1 추가, 앞 뒤로 2번반복 해야함
    count = 0
    for j in range(len(a)): # a는 계속 반복 시키면서 비교
        if a[j] != b[i+j]:
            count += 1
    count_list.append(count)

print(min(count_list))
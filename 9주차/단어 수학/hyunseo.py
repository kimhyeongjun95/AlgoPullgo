# 백준 1339 단어수학
from collections import defaultdict

N = int(input())

words = []
max_len = 0

for _ in range(N):
    temp = input()
    
    words.append(temp)
    max_len = max(max_len, len(temp))

# 각 자리수에 계산될 알파벳
calculate = [[] for _ in range(max_len)]

for word in words:
    start = max_len - len(word)
    for i in range(start, max_len):
        calculate[i].append(word[i-start])

# print(calculate)

cnt = defaultdict(int)
for j in range(max_len):
    for alpha in set(calculate[j]):
        cnt[alpha] += calculate[j].count(alpha) * 10**(max_len-1-j)

cnt_value = sorted(cnt.values(), key=lambda x : -x)
# print(cnt_value)

answer = 0
number = 9
for value in cnt_value:
    answer += number*value
    number -= 1

print(answer)
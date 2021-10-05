# 1339 단어 수학
from collections import defaultdict

n = int(input())
alpha = defaultdict(int)
word_math = []
for _ in range(n):
    word = input()
    word_math.append(word)
    word = word[::-1]
    for i in range(len(word)):
        alpha[word[i]] += 10 ** i

words = list(alpha.items())
words.sort(key=lambda x: -x[1])

alpha = defaultdict(int)
for i in range(len(words)):
    alpha[words[i][0]] = str(9 - i)

ans = 0
for word in word_math:
    temp = ''
    for num in word:
        temp += alpha[num]
    ans += int(temp)

print(ans)

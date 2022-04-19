#  백준 1759 암호 만들기

# L개의 알파벳 소문자로 구성
# 최소 한 개의 모음(aeiou)와 두 개의 자음

# 정렬된 알파벳
# 사용했을 법한 문자의 종류는 C가지

# C개의 문자들이 모두 주어졌을때, 경우의 수 모두 출력(사전순)

from itertools import combinations

l, c = map(int, input().split())
s = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']

result = []
for combo in combinations(s, l):
	count = 0
	for i in combo:
		if i in vowels:
			count += 1
	if count >= 1 and l - count >= 2:
		result.append(''.join(sorted(combo)))
result.sort()

for i in result:
	print(i)

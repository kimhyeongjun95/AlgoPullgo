# 백준 1759 암호 만들기

from itertools import combinations

L, C = map(int, input().split())
alphabet = list(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

consonant = set()
vowel = set()
for a in alphabet:
    if a in vowels:
        vowel.add(a)
    else:
        consonant.add(a)

answer = set()
# 모음 1개 뽑기
for v in vowel:
    # 자음 2개 뽑기
    for cs in combinations(consonant, 2):
        # 그 외
        n = L - 3
        rest = (vowel - set([v])) | (consonant - set(cs))

        for r in combinations(rest, n):
            temp = list(set([v]) | set(cs) | set(r))
            temp.sort()
            answer.add(''.join(temp))

for ans in sorted(answer):
    print(ans)
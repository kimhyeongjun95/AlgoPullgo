from itertools import combinations

N, M = map(int, input().split())
password = input().split()
vowels = ['a','e','i','o','u']

c, v = [], []
for p in password:
    if p in vowels:
        v.append(p)
    else:
        c.append(p)

answers = []
start = max(1, N-len(c))
end = min(len(v), N-2)
for i in range(start, end+1):
    for combi in combinations(v, i):
        for combi2 in combinations(c, N-i):
            temp = combi + combi2
            answers.append(''.join(sorted(temp)))

for answer in sorted(answers):
    print(answer)


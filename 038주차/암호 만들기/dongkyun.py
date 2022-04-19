from itertools import combinations

L,C = map(int,input().split())
alpha_list = input().split()
aeiou_list = ['a', 'e', 'i', 'o', 'u']
answer = []

for patch_note in combinations(alpha_list, 4):
    a_count = 0
    q_count = 0

    for patch in patch_note:
        if patch in aeiou_list:
            a_count += 1
        else:
            q_count += 1
    if a_count >= 1 and q_count >= 2:
        patch_note = tuple(sorted(patch_note, key=lambda x : x))
        cocoball = ''
        for pat in patch_note:
            cocoball += pat
        answer.append(cocoball)
answer.sort()

for i in answer:

    print(i)
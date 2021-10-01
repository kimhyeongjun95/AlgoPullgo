import sys
input = sys.stdin.readline


N = int(input()) 
arr = [list(input().strip()) for _ in range(N)]

alphabet = []
for word in arr:
    for a in word:
        if a not in alphabet:
            alphabet.append(a)

value_list = []
for a in alphabet:
    value = 0
    for word in arr:
        if a not in word:  # 알파벳 없으면 넘어감
            continue

        s = ""
        for w in word:
            s += "1" if w == a else "0"
        value += int(s)

    value_list.append(value)

value_list.sort(reverse=True) 

answer = 0
value = 9
for s in value_list:
    answer += value * s
    value -= 1

print(answer)
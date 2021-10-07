import sys

S = sys.stdin.readline().strip()

reverse = True
answer = ''
temp = ''
i = 0

while i < len(S):
    if S[i] == '<':
        reverse = False
    elif S[i] == '>':
        reverse = True
    
    if reverse:
        if S[i] == '>':
            answer += S[i]
        elif S[i] != ' ':
            temp += S[i]
        else:
            answer += temp[::-1] + S[i]
            temp = ''
    else:
        answer += S[i]
    
    if i+1 == len(S) or S[i+1] == '<':
        answer += temp[::-1]
        temp = ''
    
    i += 1
    
print(answer)
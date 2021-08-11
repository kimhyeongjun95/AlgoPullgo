import sys

S = sys.stdin.readline().strip()

start = 0
end = len(S)
temp = S

while temp != '_'*len(S):
    if '>' in temp:
        start = temp.find('>', start) + 1
        end = temp.find('<', start)
        if end == -1 :
            end = len(S)
        
    words = list(S[start:end].split())
    reverse = ''

    for word in words:
        reverse += word[::-1] + ' '

    S = S.replace(S[start:end], reverse.rstrip())
    temp = temp.replace(temp[:end], '_'*end)

print(S)
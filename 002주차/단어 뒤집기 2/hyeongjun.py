s = input()

result = ''

idx = 0
temp = 0
answer = list(s)
while idx < len(s):
    if s[idx] == '<':
        idx += 1
        
        while s[idx] != '>':
            idx += 1
           # answer.append(s[:idx])

    if s[idx].isalnum():
        temp = idx
        while idx < len(s) and s[idx].isalnum():
            idx += 1
        result = list(s[temp:idx])
        result.reverse()
        answer[temp:idx] = result
        # print(result)

    else:
        idx += 1

print(''.join(answer))
    


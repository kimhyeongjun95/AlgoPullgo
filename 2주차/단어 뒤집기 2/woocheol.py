# 17413 단어 뒤집기2

words = input()
stack = ''
temp = ''
ans = ''
for word in words:
    if word == '<':
        if temp:
            ans += temp
            temp = ''
        stack += word
    elif word == '>':
        stack += word
        ans += stack
        stack = ''
    elif word == ' ' and not stack:
        ans += temp + ' '
        temp = ''
    elif stack:
        stack += word
    else:
        temp = word + temp

if temp:
    ans += temp
if stack:
    ans += stack

print(ans)

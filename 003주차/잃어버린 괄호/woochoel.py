# 1541번 잃어버린 괄호
expression = input()

flag = False
ans = 0
num = ''
for s in expression:
    if s == '+' or s == '-':

        if flag and num:
            ans -= int(num)
        elif not flag and num:
            ans += int(num)
        if s == '-':
            flag = True
        num = ''
    else:
        num += s
if flag:
    ans -= int(num)
else:
    ans += int(num)

print(ans)

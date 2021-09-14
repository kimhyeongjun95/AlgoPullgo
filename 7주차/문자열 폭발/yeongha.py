# 문자열 폭발
import sys

string = list(sys.stdin.readline().strip())
bomb = list(sys.stdin.readline().strip())
new = []
l = len(bomb)
for i in string:
    new.append(i)
    if i == bomb[-1]:
        if new[-l:] == bomb:
            i = 0
            while i < l:
                new.pop()
                i += 1

if new:
    print(''.join(new))
else:
    print('FRULA')

import sys

string = [i for i in sys.stdin.readline().rstrip()]
bomb = [i for i in sys.stdin.readline().rstrip()] # 폭탄 문자열

stack = [] # 스택 만들어 주기
for s in string:
    stack.append(s)
    if stack[len(stack)-len(bomb):] == bomb: # 폭탄 문자열의 길이만큼의 스택의 끝 문자열이 폭탄 문자열이라면
        for _ in range(len(bomb)): # 폭탄 문자열의 길이 만큼 pop
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
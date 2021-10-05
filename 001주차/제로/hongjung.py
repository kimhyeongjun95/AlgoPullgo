import sys

K = int(sys.stdin.readline()) # 받아올 정수의 개수

number_list = [] # 정수를 넣을 스택
for i in range(K):
    number = int(sys.stdin.readline())
    if number:
        number_list.append(number) # 정수가 0이 아니면 스택에 추가
    else:
        number_list.pop() # 정수가 0이면 스택의 마지막 정수 빼내기

print(sum(number_list)) # 스택 안의 정수의 합
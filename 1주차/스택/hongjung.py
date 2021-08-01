import sys

N = int(sys.stdin.readline()) # 명령의 수 N 받아오기

number_list = [] # 스택 만들어주기
for i in range(N): # 명령의 수 만큼 반복 입력
    command = sys.stdin.readline().split() # push일 경우 뒤에 숫자가 들어오므로 공백으로 분리
    if command[0] == 'push':
        number_list.append(command[1]) # 스택에 숫자를 추가
    elif command[0] == 'top':
        if len(number_list):
            print(number_list[-1]) # 스택의 가장 위에(나중에) 있는 숫자 출력
        else:
            print(-1) # 스택에 숫자가 없으면 -1 출력
    elif command[0] == 'size':
        print(len(number_list)) # 스택의 길이 출력
    elif command[0] == 'empty':
        if len(number_list):
            print(0) # 스택이 비어있지 않으면 0 출력
        else:
            print(1) # 스택이 비어있으면 1 출력
    elif command[0] == 'pop':
        if len(number_list):
            print(number_list.pop()) # 스택의 가장 위에 있는 숫자를 빼내고 그 숫자를 출력
        else:
            print(-1) # 스택에 숫자가 없으면 -1 출력

# 번외로 함수로 만들어 풀이(런타임 오류로 사용 못함)
# def push(list1, number):
#     return list1.append(number)

# def pop(list1):
#     if len(list1):
#         print(list1[-1])
#         list1.pop()
#     else:
#         print(-1)

# def size(list1):
#     print(len(list1))

# def empty(list1):
#     if len(list1):
#         print(0)
#     else:
#         print(1)

# def top(list1):
#     if len(list1):
#         print(list1[-1])
#     else:
#         print(-1)

# import sys

# N = int(sys.stdin.readline())

# number_list = []
# for i in range(N):
#     command, number = sys.stdin.readline().split()

#     if command == 'push':
#         push(number_list, number)
#     elif command == 'top':
#         top(number_list)
#     elif command == 'size':
#         size(number_list)
#     elif command == 'empty':
#         empty(number_list)
#     elif command == 'pop':
#         pop(number_list)
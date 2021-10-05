import sys

N = int(sys.stdin.readline())

number_list = []
for _ in range(N):
    c = sys.stdin.readline().split()
    if c[0] == 'push':
        number_list.append(c[1])
    elif c[0] == 'pop': # 이걸 해결해야 하는데...
        if number_list:
            print(number_list.pop(0))
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(number_list))
    elif c[0] == 'empty':
        if number_list:
            print(0)
        else:
            print(1)
    elif c[0] == 'front':
        if number_list:
            print(number_list[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if number_list:
            print(number_list[-1])
        else:
            print(-1)
import sys
N = int(sys.stdin.readline())
result_list = []

for _ in range(N):
    command = sys.stdin.readline().split()
    order = command[0]

    if order == "push":
        result_list.append(int(command[1]))
    elif order == "pop":
        if result_list:
            print(result_list[-1])
            del result_list[-1]
        else:
            print(-1)
    elif order == "size":
        print(len(result_list))
    elif order == "empty":
        if result_list:
            print(0)
        else:
            print(1)
    elif order == "top":
        if result_list:
            print(result_list[-1])
        else:
            print(-1)
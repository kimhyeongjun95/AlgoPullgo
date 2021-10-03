import sys

width, height = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
stores = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 1은 북, 2는 남, 3은 서, 4는 동
start = list(map(int, sys.stdin.readline().split()))

result = []
if start[0] == 1:
    for i in range(N):
        if stores[i][0] == 2:
            tmp = height
            if (width - start[1]) + (width - stores[i][1]) > start[1] + stores[i][1]:
                tmp += start[1] + stores[i][1]
            else:
                tmp += (width - start[1]) + (width - stores[i][1])
        elif stores[i][0] == 3:
            tmp = start[1] + stores[i][1]
        elif stores[i][0] == 4:
            tmp = (width - start[1]) + stores[i][1]
        else:
            tmp = abs(start[1] - stores[i][1])
        result.append(tmp)
elif start[0] == 2:
    for i in range(N):
        if stores[i][0] == 1:
            tmp = height
            if (width - start[1]) + (width - stores[i][1]) > start[1] + stores[i][1]:
                tmp += start[1] + stores[i][1]
            else:
                tmp += (width - start[1]) + (width - stores[i][1])
        elif stores[i][0] == 3:
            tmp = start[1] + (height - stores[i][1])
        elif stores[i][0] == 4:
            tmp = (width - start[1]) + (height - stores[i][1])
        else:
            tmp = abs(start[1] - stores[i][1])
        result.append(tmp)
elif start[0] == 3:
    for i in range(N):
        if stores[i][0] == 4:
            tmp = width
            if (height - start[1]) + (height - stores[i][1]) > start[1] + stores[i][1]:
                tmp += start[1] + stores[i][1]
            else:
                tmp += (height - start[1]) + (height - stores[i][1])
        elif stores[i][0] == 1:
            tmp = start[1] + stores[i][1]
        elif stores[i][0] == 2:
            tmp = (height - start[1]) + stores[i][1]
        else:
            tmp = abs(start[1] - stores[i][1])
        result.append(tmp)
else:
    for i in range(N):
        if stores[i][0] == 3:
            tmp = width
            if (height - start[1]) + (height - stores[i][1]) > start[1] + stores[i][1]:
                tmp += start[1] + stores[i][1]
            else:
                tmp += (height - start[1]) + (height - stores[i][1])
        elif stores[i][0] == 1:
            tmp = start[1] + (width - stores[i][1])
        elif stores[i][0] == 2:
            tmp = (height - start[1]) + (width - stores[i][1])
        else:
            tmp = abs(start[1] - stores[i][1])
        result.append(tmp)

print(sum(result))
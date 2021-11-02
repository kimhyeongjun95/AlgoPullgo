import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    numbers = [sys.stdin.readline().rstrip() for _ in range(N)]
    numbers.sort()

    for i in range(N-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            print('NO')
            break
    else:
        print('YES')




import sys

def is_consistency(numbers):

    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] == numbers[j][:len(numbers[i])]:
                return 'NO'
    
    return 'YES'


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [sys.stdin.readline().rstrip() for _ in range(n)]
    numbers = sorted(numbers, key=lambda x: len(x))

    print(is_consistency(numbers))
    
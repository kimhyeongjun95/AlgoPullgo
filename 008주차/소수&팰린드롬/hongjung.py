import sys

N = int(sys.stdin.readline())

if N == 1: # N이 1이면 2로 바꿔서 2가 나오게 만듦
    N = 2
result = ''
i = 0
while True:
    n = str(N + i)
    if len(n) % 2: # 길이가 홀수일 때
        for j in range(len(n)//2):
            if n[j] != n[len(n)-j-1]:
                break
        else:
            for j in range(2, N + i): # 소수 판별
                if (N + i) % j == 0:
                    break
            else:
                result = n
                break
    else: # 길이가 짝수일 때
        for j in range(len(n)//2+1):
            if n[j] != n[len(n)-j-1]:
                break
        else:
            for j in range(2, N + i): # 소수 판별
                if (N + i) % j == 0:
                    break
            else:
                result = n
                break
    i += 1

print(result)
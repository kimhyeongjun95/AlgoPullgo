import sys
input = sys.stdin.readline
N = int(input())

if N == 1:
    print(2)
    
else:
    while True:
        flag = True

        if str(N) == str(N)[::-1]:
            for i in range(2, N):
                if not N % i:
                    flag = False
                    break
            
            if flag:
                print(N)
                break
        N += 1
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num_lst = []

    for _ in range(N):
        num_lst.append(input().strip())
    
    num_lst = sorted(num_lst)
    print(num_lst)
    flag = 0

    for i in range(N-1):
        if num_lst[i] == num_lst[i+1][:len(num_lst[i])]:
            print("NO")
            flag = 1
            break

    if flag == 0:
        print("YES")


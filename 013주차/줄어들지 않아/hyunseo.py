# 백준 2688 줄어들지 않아

def counting(n):
    if n == 1:
        return 10

    cnt = {
        0: 10, 1: 9, 2: 8, 3: 7, 4: 6,
        5: 5, 6: 4, 7: 3, 8: 2, 9: 1
    }

    result = {}

    for _ in range(n-2):
        for num in range(10):
            temp = 0
            for t in range(num, 10):
                temp += cnt[t]

            result[num] = temp
        
        cnt = result
        result = {}
    
    return sum(cnt.values())


for _ in range(int(input())):
    n = int(input())

    print(counting(n))
# 백준 2473 세 용액
N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

min_diff = float('inf')
answer = []

for j in range(N-2):
    if j > 0 and liquid[j] == liquid[j-1]:
        continue

    l = j + 1
    r = N - 1

    while l < r:
        total = liquid[j] + liquid[l] + liquid[r]
        diff = abs(total)

        if diff < min_diff:
            min_diff = diff
            answer = [j, l, r]
            
        if total > 0:
            r -= 1
        elif total < 0:
            l += 1
        else:
            break
    
    if not min_diff:
        break

print(liquid[answer[0]], liquid[answer[1]], liquid[answer[2]])
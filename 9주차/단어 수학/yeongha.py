N = int(input())
words = []
for _ in range(N):
    words.append(list(input()))
alphas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

lst = []
for a in alphas:
    total = 0
    for word in words:
        for i, b in enumerate(word[::-1]):
            if a == b:
                total += 10**i
    lst.append(total)
lst.sort(reverse=True)

num = 9
ans = 0
for item in lst:
    if item == 0:
        break
    ans += num*int(item)
    num -= 1
print(ans)





# 1747번 소수 & 펠린드롬

is_prime = [True for _ in range(1005000)]
is_prime[0], is_prime[1] = False, False

for i in range(2, 1005000):
    if is_prime[i]:
        for j in range(2*i, 1005000, i):
            is_prime[j] = False

n = int(input())
for num in range(n, 1005000):
    if str(num) == str(num)[::-1] and is_prime[num]:
        print(num)
        break

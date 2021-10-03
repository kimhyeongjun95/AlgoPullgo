# 백준 2960 에라토스테네스의 체

def is_prime(number):
    for i in range(2, number):
        if not number%i:
            return False
    else:
        return True


N, K = map(int, input().split())

numbers = []
for i in range(2, N+1):
    numbers.append(i)

i = 0 
cnt = 0
while cnt < K:
    temp = numbers[i]
    if is_prime(temp):
        for number in numbers:
            if not number%temp:
                numbers.remove(number)
                cnt += 1
                if cnt == K:
                    break
    else:
        i += 1

print(number)
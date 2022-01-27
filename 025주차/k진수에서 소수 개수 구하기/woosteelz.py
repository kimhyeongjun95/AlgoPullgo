import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def change_k(num, k):
    answer = ''
    while num:
        num, mod = divmod(num, k)
        answer += str(mod)
    return answer[::-1]


def solution(n, k):
    answer = 0
    n = change_k(n, k)

    prime_list = n.split('0')

    for prime in prime_list:
        if prime and is_prime_number(int(prime)):
            answer += 1

    return answer

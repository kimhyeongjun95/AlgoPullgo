# 에라토스테네스의 체
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def eratostenes(N, K):
    cnt = 0
    prime = [i for i in range(2,N+1)]
    while prime:
        n = prime[0]
        if is_prime(n):
            m = 1
            while n*m <= N:
                if n*m in prime:
                    prime.remove(n*m)
                    cnt += 1
                    if cnt == K:
                        return n*m
                m += 1


N, K = map(int, input().split())
print(eratostenes(N, K))
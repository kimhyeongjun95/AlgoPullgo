# 테케 1번 시간초과
def solution(n, k):
    def change_num(n, k):
        result = ''
        while n:
            result  = str(n % k) + result
            n //= k
        return result
    
    def find_prime_num(n):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    
    num = change_num(n, k)
    num = num.split('0')
    nums = []
    for n in num:
        if n:
            nums.append(int(n))

    answer = 0
    for n in nums:
        if n > 1 and find_prime_num(n):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))
# 프로그래머스 k진수에서 소수 개수 구하기

def change_number(number, k):
    result = ''
    
    while number:
        result += str(number%k)
        number //= k
    
    return result[::-1]

# def is_prime(number):
#     if number == 1:
#         return False
    
#     prime = [True for _ in range(number+1)]
    
#     for n in range(2, int(number**0.5)+1):
#         if prime[n]:
#             if number%n == 0:
#                 return False
            
#             for not_prime in range(n+n, number+1, n):
#                 prime[not_prime] = False
    
#     return prime[number]


def is_prime(number):
    if number == 1:
        return False
    
    for n in range(2, int(number**0.5)+1):
        if number%n == 0:
            return False
    
    return True
    
    
def solution(n, k):
    string = change_number(n, k)
    
    answer = 0
    for number in string.split('0'):
        if number and is_prime(int(number)):
            answer += 1
    
    return answer
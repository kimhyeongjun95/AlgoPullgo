# 백준 1747 소수&팰린드롬

N = int(input())

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if not number%i:
            return False
    
    return True


while True:
    if is_prime(N):
        if str(N) == str(N)[::-1]:
            print(N)
            break
        else:
            N += 1
    else:
        N += 1
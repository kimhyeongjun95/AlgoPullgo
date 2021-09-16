def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

def prime(n):
    m = int(n**0.5)
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True

N = int(input())
n = N
while True:
    if n == 1:
        print(2)
        break
    elif n == 2:
        print(n)
        break
    elif n % 2 and prime(n) and palindrome(n):
        print(n)
        break
    n += 1

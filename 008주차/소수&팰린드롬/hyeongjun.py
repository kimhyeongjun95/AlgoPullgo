# 백준 1747 & 팰린드롬

# 팰린드롬 : 뒤집어도 같은 수

# n 이상이면서 소수이면서 
# 팰린드롬이면서 가장 작은 수 구하기

import sys
import math
input = sys.stdin.readline

def prime_check(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(number))+1):
            if number % i == 0:
                return False
    return True

def palindrome(number):
    number = str(number)
    if number[::-1] == number:
       return True
    return False

n = int(input())

while True:
    if prime_check(n) and palindrome(n):
        break
    n += 1
print(n)


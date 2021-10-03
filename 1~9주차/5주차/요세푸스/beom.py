import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = [i for i in range(1, N+1)]
result = []

n = K - 1
while people:
    if len(people) > n: 
        result.append(people.pop(n))
        n += K - 1
    
    elif len(people) <= n:
        n = n % len(people)
        result.append(people.pop(n))
        n += K - 1

print("<", ', '.join(str(i) for i in result), ">", sep = '')
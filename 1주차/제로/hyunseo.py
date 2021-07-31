K = int(input())

result = []

for _ in range(K) :
    number = int(input())

    if number == 0 :
        result.pop()
    else :
        result.append(number)

print(sum(result))
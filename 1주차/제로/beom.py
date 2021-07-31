T = int(input())
result = []
for tc in range(T):
    numbers = int(input())
    if numbers:
        result.append(numbers)
    else:
        result.pop()
print(sum(result))
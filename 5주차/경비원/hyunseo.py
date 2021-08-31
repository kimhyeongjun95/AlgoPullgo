x, y = map(int, input().split())
N = int(input())

stores = []
for i in range(N+1):
    way, distance = map(int, input().split())

    if way == 1:
        temp = distance
    elif way == 2:
        temp = 2*x + y - distance
    elif way == 3:
        temp = 2*x + 2*y - distance
    else:
        temp = x + distance
    
    if i == N:
        curr = temp
    else:
        stores.append(temp)

lenght = 2*x + 2*y
total = 0
for store in stores:
    if curr < store:
        if store - curr < curr + (lenght-store):
            total += store - curr
        else:
            total += curr + (lenght-store)
    else:
        if curr - store < store + (lenght-curr):
            total += curr - store
        else:
            total += store + (lenght-curr)

print(total)
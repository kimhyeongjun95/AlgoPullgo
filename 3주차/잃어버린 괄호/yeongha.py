a = input().split('-')
count = 0

lst = list(map(int,a[0].split('+')))
count += sum(lst)

for i in a[1:]:
    lst = list(map(int,i.split('+')))
    count -= sum(lst)
print(count)
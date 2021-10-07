import sys
input = sys.stdin.readline
arr = input().split('-')
result = [] 

for i in arr:     # 55-50+40
    total = 0
    arr_1 = i.split('+')
    
    for j in arr_1:    
        total += int(j)  
    result.append(total)
 
num = result[0]
for i in range(1, len(result)):
    num -= result[i]
print(num)

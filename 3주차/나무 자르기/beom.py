def binary_search(height_list, target):
    start = 1
    end = max(height_list)

    while start <= end:
        middle = (start + end) // 2   
        total = 0

        # 총 잘린 나무 길이
        for i in height_list:
            if i > middle:
                total += i - middle   
        
        if total >= target:
            start = middle + 1
        else:
            end = middle -1
    
    return end

N, M = map(int, input().split())
height_list = list(map(int, input().split()))

print(binary_search(height_list, M))

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int,input().split()))

left = 0 
right = len(heights) - 1
left_max, right_max = heights[left], heights[right]
total = 0

while left < right:
    left_max = max(left_max, heights[left])
    right_max = max(right_max, heights[right])
    
    if left_max <= right_max:
        total += left_max - heights[left]
        left += 1
    else:
        total += right_max - heights[right]
        right -= 1
print(total)
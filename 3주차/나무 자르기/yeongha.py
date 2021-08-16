import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

def tree_cut(start, end, lst, need):
    while start <= end:
        middle = (start + end)//2
        total = 0

        for i in lst:
            if i > middle:
                total += i - middle

        if total == need:
            return middle # 딱 M미터의 나무를 가져갈 수 있는 경우

        if total >= need:
            start = middle + 1
        else:
            end = middle - 1
            
    return end # M미터의 나무를 가져갈 수 없는 경우 최대한 적게 가져가기 위해
    
print(tree_cut(0,max(tree),tree,M))
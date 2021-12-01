from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
opp_cnt = list(map(int, input().split()))
opp = []
for i, cnt in enumerate(opp_cnt):
    opp += [i] * cnt
max_result, min_result = float('-inf'), float('inf')
opp_case = set(permutations(opp, len(opp)))

for opp_list in opp_case:
    result = numbers[0]
    for i in range(N-1):
        if opp_list[i] == 0:
            result += numbers[i+1]
        elif opp_list[i] == 1:
            result -= numbers[i+1]
        elif opp_list[i] == 2:
            result *= numbers[i+1]
        else:
            if result < 0:
                result = -(-result//numbers[i+1])
            else:
                result //= numbers[i+1]
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
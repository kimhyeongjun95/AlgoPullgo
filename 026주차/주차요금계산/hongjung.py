from collections import defaultdict
import math

def solution(fees, records):
    num_dict = defaultdict(list)
    nums = []
    for record in records:
        if record[6:10] not in nums:
            nums.append(record[6:10]) 
        num_dict[record[6:10]].append(int(record[:2]) * 60 + int(record[3:5]))
    
    nums.sort()
    answer = []
    for num in nums:
        if len(num_dict[num]) % 2:
            num_dict[num].append(23 * 60 + 59)

        tmp = 0
        for i in range(1, len(num_dict[num]) + 1, 2):
            tmp += num_dict[num][i] - num_dict[num][i-1]

        result = 0
        if tmp > fees[0]:
            result = fees[1] + math.ceil((tmp - fees[0]) / fees[2]) * fees[3]
        else:
            result = fees[1]

        answer.append(result)

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
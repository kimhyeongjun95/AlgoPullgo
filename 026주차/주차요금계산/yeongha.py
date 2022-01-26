from collections import defaultdict
import math

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees
    cars = {}
    total = defaultdict(int)
    for rec in records:
        time, car, state = rec.split()
        if state == 'IN':
            cars[car] = time
        else:
            out_h, out_m = map(int, time.split(':'))
            in_h, in_m = map(int, cars[car].split(':'))
            total[car] += (out_h * 60 + out_m) - (in_h * 60 + in_m)
            del cars[car]

    for car, time in cars.items():
        in_h, in_m = map(int, time.split(':'))
        total[car] += 1439 - (in_h * 60 + in_m)

    for car, time in total.items():
        if time <= basic_time:
            total[car] = basic_fee
        else:
            fee = basic_fee + math.ceil((time - basic_time)/unit_time) * unit_fee
            total[car] = fee

    answer = [value for key, value in sorted(total.items(), key=lambda x : x[0])]
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
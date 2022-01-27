from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    temp = []
    car_inout = defaultdict(list)

    for record in records:
        time, car_num, in_out = record.split()
        car_inout[car_num].append(time)

    for key, value in car_inout.items():
        parking_time = 0
        # 입출차 기록이 홀수일 경우 -> 23:59 추가
        if len(value) % 2:
            value.append('23:59')

        for i in range(0, len(value), 2):
            parking_time += (int(value[i+1][:2]) * 60 + int(value[i+1][3:])) - \
                (int(value[i][:2]) * 60 + int(value[i][3:]))
        print(parking_time)

        if parking_time > fees[0]:
            temp.append(
                [key, fees[1] + math.ceil((parking_time - fees[0]) / fees[2]) * fees[3]])
        else:
            temp.append([key, fees[1]])
    temp.sort()
    for tp in temp:
        answer.append(tp[1])

    return answer

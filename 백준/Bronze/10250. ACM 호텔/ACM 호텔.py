# T는 테스트 데이터의 개수
#H: 호텔의 층수, W: 각 층의 방수, N: 몇 번째 손님인지
import math

T= int(input())

#num-int(num) 을 통해 num의 소수 부분을 얻기, 소수 부분이 0.5보다 크다면 반올림 
def custom_round(num):
    return math.ceil(num) if num - int(num) >= 0.1 else math.floor(num)

for i in range(T):
    H, W, N= map(int, input().split())

    floor = N % H
    if floor == 0:
        floor = H

    #반올림
    room_number = math.ceil(N / H)
    if room_number < 10:
        room_number = str(floor) + '0' + str(room_number)
    else:
        room_number = str(floor) + str(room_number)

    print(room_number)
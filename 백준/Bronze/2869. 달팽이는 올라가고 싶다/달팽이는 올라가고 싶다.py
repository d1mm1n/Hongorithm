A, B, V = map(int, input().split())

total_distance = V - A
move_distance = A - B

day = total_distance // move_distance
if total_distance % move_distance > 0:
    day += 1

print(day + 1)

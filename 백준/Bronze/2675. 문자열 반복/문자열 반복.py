n = int(input())

for i in range(n):
    num, string = input().split()
    num = int(num)
    for char in string:
        #char*num 은 char을 num번 반복한 문자열을 생성, 이건 몰랐음
        #end=''는 줄바꿈 없이 출력하려고
        print(char * num, end='')
    print()  # 줄바꿈
num= input().split()

#정수 뒤집기
num[0]=num[0][::-1]
num[1]=num[1][::-1]
# 정수로 변경
num= [int(x) for x in num] 

print(max(num))
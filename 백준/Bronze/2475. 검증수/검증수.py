num=input().split()

#정수로 변환
num= [int(x) for x in num]
result=0
for i in range(5):
    result+=num[i]*num[i]

print(result%10)
# 소수 찾기
a=input()
a=int(a)

count=0
num=[]
num=input().split()
num=list(map(int,num))


#소수 : 1과 자기 자신 외에는 나누어 떨어지지 않음
#num에 3 5 가 들어가 있을 때 i =3, 5, 2번 반복
for i in num:
    flag=0
    for k in range(i):
        left=i%(k+1)
        if left==0:
            flag=flag+1
       
    if flag==2:
        count=count+1

print(count)
            
    
num=input()
num=int(num)

pre=0
sum=1
a=0

for i in range(num-1):
    a=pre+sum
    pre=sum
    sum=a

if num==1:
    print(1);
else:
    print(a)
num = input("")
num = int(num)
f = int(num / 10)
l = int(num % 10)
total = f + l


count = 0
new=-1
while num != new:
    count=count+1
    if(total<10):
        new=l*10+total
    elif(total>=10):
        new=(total%10)+l*10
    
    f=int(new/10)
    l=int(new%10)
    total=f+l

print(count)

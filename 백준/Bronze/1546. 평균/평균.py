n=int(input())

num= input().split()

re=0
num=[int(x) for x in num]
m=max(num)

for i in range(n): 
    re+=num[i]/m*100
    
print(re/n)
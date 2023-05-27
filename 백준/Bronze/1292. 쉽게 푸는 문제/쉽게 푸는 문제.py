start, end=input().split()
start=int(start)
end= int(end)

num=[]
n=0
for i in range(end):
    n+=1
    for k in range(i+1):
        num.append(n)

result=0
for i in range(start-1,end):
    result+=num[i]
print(result)
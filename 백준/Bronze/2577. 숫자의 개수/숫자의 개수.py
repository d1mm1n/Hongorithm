mul=1
result=[]
for i in range(3):
    num=int(input())
    mul*=num
    
    
mul=str(mul)    
# 하나의 정수를 자릿수 별로 나눠서 리스트에 저장하기
mul=list(map(int,str(mul)))

for i in range(10):
    count=0
    for k in range(len(mul)):
        if mul[k]==i:
            count+=1
            
    result.insert(i,count)  
    print(result[i])
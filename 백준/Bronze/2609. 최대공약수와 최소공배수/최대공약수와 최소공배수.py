num1, num2 = input().split()

num1=int(num1)
num2=int(num2)

lnum1=[]
lnum2=[]
#최대 공약수 구하기
for i in range(num1):
    if num1%(i+1)==0:
        lnum1.append(i+1)
        
for i in range(num2):
    if num2%(i+1)==0:
        lnum2.append(i+1)
        
def find_duplicates(list1, list2):
    return [item for item in list1 if item in list2]

m=max(find_duplicates(lnum1, lnum2))
print(m)

# 최소 공배수 구하기
s=(num1*num2)//m
print(s)
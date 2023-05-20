num=[]
rnum=[]
while True:
    
    a= input()
    if (a=='0'):
        break
    num.append(int(a))
    
    digits = list(str(a))
    digits.reverse()
    reversed_num = int(''.join(digits))
    
    rnum.append(reversed_num)


for i in range(len(num)):
    if num[i]==rnum[i]:
        print("yes")
    else:
        print("no")


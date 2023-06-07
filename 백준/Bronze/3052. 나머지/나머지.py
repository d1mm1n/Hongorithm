left=[]
for i in range(10):
    num=int(input())
    left.append(num%42)

# 중복 제거
result=list(set(left))
print(len(result))
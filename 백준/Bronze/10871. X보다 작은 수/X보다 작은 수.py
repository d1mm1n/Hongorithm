n, X= input().split()
n=int(n)
X=int(X)
num=input().split()

num=[int(x) for x in num]

new=[]
k=0
for i in range(n):
    if num[i]<X:
        new.append(num[i])

print(*new)
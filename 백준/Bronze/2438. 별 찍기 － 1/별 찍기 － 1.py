star=[]
n=int(input())

for i in range(n):
    star.append("*")
    # 출력 할 때 공백 없애려고 sep 사용!
    print(*star,sep='')

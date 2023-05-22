num=input()
n=list(map(int,num))
n.sort(reverse=True)

join_n=int(''.join(str(num) for num in n))
print(join_n)
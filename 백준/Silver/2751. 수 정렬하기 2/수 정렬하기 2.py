#python3 으로 제출 시에 시간 초과가 떠서 pypy3으로 제출 했더니 됨,,
n=int(input())

num=[]

for i in range(n):
    num.append(int(input()))

for i in sorted(num):
        print(i)

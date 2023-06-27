#이항 계수 구하기
#첫번째 입력에서 N, K를 입력 받기

N,K=map(int,input().split())

#N이 위
n=1
# N!
for i in range(N):
    n*=i+1

k=1
#K!
for i in range(K):
    k*=i+1


tmp=1
#N-K!
for i in range(N-K):
    tmp*=i+1

result=n/(k*tmp)
print(int(result))
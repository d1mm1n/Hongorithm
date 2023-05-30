"""
n = int(input())
num=input()

k=[]
k=num.split()
print(k)

print("{} {}".format(min(k),max(k)))
"""
#처음에는 위의 코드로 작성 -> mix, max 값이 똑바로 나오지 않음 -> 이유: int 타입으로 저장을 안해서 ,,,

n = int(input())
num = input()

k = num.split()
k = [int(x) for x in k]  # 문자열을 정수로 변환

print("{} {}".format(min(k), max(k)))
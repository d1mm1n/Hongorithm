#단어 정렬
#조건1. 길이가 짧은 것부터
#조건2. 길이가 같으면 사전 순으로
num=int(input())
strlist=[]

for i in range(num):
    strlist.append(input())

newlist=[]

#사전 순으로 정렬
strlist.sort()

#key로 len 함수를 전달해주면 Iterable한 자료형의 원소에 대해 해당 함수를 적용한 값을 토대로 min을 찾아준다,,,,?>?>?>?>??무슨말이지 여튼 그렇댄다.
for i in range(len(strlist)):
    min_str= min(strlist, key=len)
    newlist.append(min_str)
    strlist.remove(min_str)

#처음에는 set을 사용해서 중복 제거를 했는데 set 은 순서를 고려하지 않아서 뒤죽박죽임
#따라서 dict.fromkeys를 사용하여 기존 리스트의 순서를 유지하고 중복제거
result=list(dict.fromkeys(newlist))
for k in result:
    print(k)

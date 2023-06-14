s=input()
#문자열을 문자 하나하나 리스트에 저장
#저장 할때 그냥 다 소문자로 저장해서 대문자 소문자 구분 안하기
s=[str(x).lower() for x in s]

from collections import Counter

def count_duplicates(arr):
    #collections.Counter를 사용하여 리스트 arr의 각 문자의 개수를 세는 부분
    #counts에는 각 문자가 키, 값으로 저장 된다.
    counts = Counter(arr)
    #counts.items() 는 닥셔너리의 값을 가져옴
    #{item: count}는 추출 된 문자와 해달 개수를 키-값 쌍으로 갖는 딕셔너리를 생성
    duplicates = {item: count for item, count in counts.items() if count > 0}
    m = max(duplicates.values())
    result = [key for key, value in duplicates.items() if value == m]

    if len(result) > 1:
        print('?')
    else:
        print(result[0].upper())


count_duplicates(s)
    




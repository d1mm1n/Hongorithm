n=int(input())

q=[]


for i in range(n):
    score=0
    count=0
    q=(input())
    for k in q:
        if k=='O':
            count+=1
            score+=count
        elif k=='X':
            count=0
    print(score)
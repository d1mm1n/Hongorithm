person=[]
b=0
h=0
r=0
for i in range(4):
    b,h=input().split()
    h= int(h)
    b=int(b)
    r+=(h-b)
    person.append(r)
  
print(max(person))
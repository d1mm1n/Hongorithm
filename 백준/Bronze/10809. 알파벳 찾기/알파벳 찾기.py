import string
st=input()

#a~z까지 하나씩 꺼내서 반복
for letter in string.ascii_lowercase:
    flag=0
    for i in st:
        if i==letter:
            flag=1
    if flag==1:
        print(st.index(letter), end=" ")
    else:
        print("-1", end=" ")
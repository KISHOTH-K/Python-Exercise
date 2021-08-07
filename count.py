taken_str="google.com"
d={}
for i in taken_str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)



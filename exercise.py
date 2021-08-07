list=[]
n=int(input("enter the number"))
for i in range(0,n):
    a=int(input())
    list.append(a)

print(list)


k=input("enter the number")
values=k.split(",")
tuple=tuple(values)
print("Values:",values)
print("tup:",tuple)

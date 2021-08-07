inp=input("enter a string")
digits=letters=0
for i in inp:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
    else:
        pass
print("Letters: ",letters)
print("Digits: ",digits)
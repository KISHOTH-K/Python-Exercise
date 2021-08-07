def com_num(list1,list2):
    result=False
    for a in list1:
        for b in list2:
            if a==b:
                result=True
                return result
print(com_num([7,8,4,6,1],[8,0,5,2,3]))


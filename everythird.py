def every_third(int_list):
    posi=3-1
    index=0
    leng=(len(int_list))
    while leng>0:
        index=(posi+index)%leng
        print(int_list.pop(index))
        leng=leng-1
l=[5,1,6,2,9,3,0,7,4,8]
every_third(l)



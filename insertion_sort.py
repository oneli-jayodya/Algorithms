def insertion(list_a):
    idx_length=range(1,len(list_a))
    for i in idx_length:
        value=list_a[i]

        while list_a[i-1]>value and i>0:
            list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
            i=i-1

    return list_a

print(insertion([2,5,7,1,9,3,6]))
                                                     
                     

def bubble(list_a):
    idx_length=len(list_a)-1
    sorted=False

    while not sorted:
        sorted=True
        for i in range(0,idx_length):
            if list_a[i]>list_a[i+1]:
                sorted = False
                list_a[i],list_a[i+1] = list_a[i+1],list_a[i]
    return list_a

print(bubble([3,5,6,2,7,1,8,4]))

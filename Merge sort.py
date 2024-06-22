def merge_sort(arr):
    
    if len(arr)>1:
        
        left= arr[:len(arr)//2]
        right= arr[len(arr)//2:]

        #recursion
        merge_sort(left)
        merge_sort(right)

        #merge
        l=0
        r=0
        m=0

        while l < len(left) and r<len(right):
            if left[l] < right[r]:
                arr[m]= left[l]
                l+=1
            else:
                arr[m] = right[r]
                r+=1
            m+=1

        while l < len(left):
            arr[m] = left[l]
            l+=1
            m+=1

        while r<len(right):
            arr[m]= right[r]
            r+=1
            m+=1

array=[2,3,4,5,1,6,9,10]
print(" Before sort : ")
print(array)
merge_sort(array)
print("After merge sort :")
print(array)
                

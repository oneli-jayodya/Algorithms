array = [4,9,3,6,2]
print("Before array: ")
print(array)

for i in range(len(array)):
    
    min_index = i
    
    for j in range(i+1, len(array)):
        
        if array[j]< array[min_index]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print("After selection sort: ")
print(array)

def partition(array, left, right):
    pivot = array[left]
    start = left + 1
    end = right

    while True:

        while start <= end and array[start] <= pivot:
            start = start + 1

        while start <= end and array[end] > pivot:
            end = end - 1

        if start < end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[left], array[end] = array[end], array[left]
    return end


def quickSort(array, start, end):
    if start >= end:
        return

    i = partition(array, start, end)
    quickSort(array, start, i-1)
    quickSort(array, i+1, end)


array = [21, 23, 25, 17, 18, 9, 24]
print("Before Sorting : ")
print((array))

left = 0
right = len(array)-1
quickSort(array, left, right)
print("After Sorting : {}".format(array))

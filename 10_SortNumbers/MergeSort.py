def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array
    
def merge(array, start, mid, end):
    left = []
    for i in range(start, mid+1):
        left.append(array[i])
    
    right = []
    for i in range(mid+1, end+1):
        right.append(array[i])
    
    # print("left, ", left, "right, ", right)
    i=0
    j=0
    k=start
    while i <= mid-start and j <= end-mid-1:
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while i <= mid-start:
        array[k] = left[i]
        i += 1
        k += 1
    
    while j <= end-mid-1:
        array[k] = right[j]
        j += 1
        k += 1
    
    # print("returning", array)
    return array
    
    
def mergeSort(array, start, end):
    if start >= end:
        return array
    if end-start == 1:
        if array[end] > array[start]:
            return array
        else:
            return swap(array, end, start)
    
    mid = (start+end)//2
    
    array = mergeSort(array, start, mid)
    array = mergeSort(array, mid+1, end)
    return merge(array, start, mid, end)
    
a = [1,32,4,1,4,24,4, 0, 100, 11, 3, 0]
# a = [3,2,1,4,5,199]
print(mergeSort(a, 0, len(a)-1))



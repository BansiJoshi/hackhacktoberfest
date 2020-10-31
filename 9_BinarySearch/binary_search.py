
def binary_search(array, start, end, val):
    if start > end:
        return -1
    if start == end:
        if array[start] == val:
            return start
        else:
            return -1

    mid = (start+end)//2
    if array[mid] == val:
        return mid

    if array[mid] > val:
        return binary_search(array, start, mid-1, val)
    else:
        return binary_search(array, mid+1, end, val)

# TODO: Take this values from user
a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,8,9,100]

print(binary_search(a, 0, len(a), 2))
print(binary_search(a, 0, len(a), 1))
print(binary_search(a, 0, len(a), 0))
print(binary_search(b, 0, len(b), 100))






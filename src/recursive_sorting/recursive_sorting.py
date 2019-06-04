# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j = 0
    k = 0
    for i in range(0, len(merged_arr)):
        if j == len(arrA) and k < len(arrB):
            merged_arr[i] = arrB[k]
            k += 1
        elif k == len(arrB) and j < len(arrA):
            merged_arr[i] = arrA[j]
            j += 1
        elif arrA[j] < arrB[k]:
            merged_arr[i] = arrA[j]
            j += 1
        else:
            merged_arr[i] = arrB[k]
            k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    print('half = ', half)
    left = merge_sort(arr[:half])
    print("left = ", left)
    right = merge_sort(arr[half:])
    print("right = ", right)
    return merge(left, right)

merge_sort([3,2,5,7,8,10,22,1,15])


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

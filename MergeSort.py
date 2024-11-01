def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sorted_left = mergesort(leftHalf)
    sorted_right = mergesort(rightHalf)

    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = list(map(int,input("Enter the Array you want to Sort : ").split()))
sortedArr = mergesort(unsortedArr)
print("Sorted Array : ", sortedArr)



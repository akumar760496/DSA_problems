def mergeTwoSortedArray(arr1 , m , arr2 , n):
    #arr1 -> array 1 in sorted order need to merge m elements of array 1 in resultant array
    #arr2 -> array 2 in sorted order need to merge n elements of array 2 in resultant array 

    output_arr = [0]*(m+n)
    if m != 0:
        for i in range(m):
            output_arr[i] = arr1[i]

    if n != 0:
        for i in range(n):
            output_arr[i+m] = arr2[i]

    output_arr.sort()
    return output_arr

def mergeTwoSortedArrayWithoutExtraSpaces(arr1 , m , arr2 , n):
    for j in range(n):
        arr1[m+j] = arr2[j]
    arr1.sort()
    return arr1

if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    m = 3
    arr2 = [2,5,6]
    n = 3

    arr = mergeTwoSortedArrayWithoutExtraSpaces(arr1=arr1 , m = m , arr2=arr2 , n = n)
    for i in range(len(arr)):
        print(arr[i] , end=" ")
    print()
    
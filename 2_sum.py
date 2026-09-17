def twoSum(arr, target):
    """
    This function takes an array of intergers and a target integer as input. It returns the indices of the two numbers in the array that add up to the target integer. 
    If no such pair exists, it returns an empty list.
    """

    arr_length = len(arr)
    sum_exists = False;

    for i in range(arr_length):
        for j in range(i + 1, arr_length):
            if arr[i] + arr[j] == target:
                sum_exists = True
                return (sum_exists , [i, j])
            else:
                sum_exists = False
                return (sum_exists, [])

"""better approach using binary search"""
def binarySearch(arr , left , right , target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return (True , mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return (False , -1)

def twoSumBinarySearch(arr, target):
    arr.sort()
    arr_length = len(arr)
    sum_exists = False;

    for i in range(arr_length):
        complement = target - arr[i]
        found, index = binarySearch(arr, i + 1, arr_length - 1, complement)
        if found:
            sum_exists = True
            return (sum_exists , [i, index])
        else:
            sum_exists = False
            return (sum_exists, [])
        

"""Third better approach using Sorting and two pointers"""

def twoSumUsingSortingAndTwoPointers(arr, target):
    arr.sort()
    left = 0 
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return (True , [left, right])
        elif sum < target:
            left += 1
        else:
            right -= 1

    return (False, [])


"""
best and optimal approach using hashset
"""

def twoSumUsingHashSet(arr, target):
    s = set()
    for num in arr:
        complement = target - num
        if complement in s:
            return (True , [arr.index(complement), arr.index(num)])
        s.add(num)
    return (False, [])




if __name__ == "__main__":
    # arr = [2, 7, 11, 15]
    # target = 9
    arr = [0, -1, 2, -3, 1]
    target = -2
    #result = twoSum(arr, target)
    #result = twoSumBinarySearch(arr, target)
    #result = twoSumUsingSortingAndTwoPointers(arr, target)
    result = twoSumUsingHashSet(arr, target)
    print(result)
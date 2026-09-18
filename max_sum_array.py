def maxSumArray(arr):
    arr_length = len(arr)
    result = arr[0]
    for i in range(arr_length):
        current_sum = 0
        for j in range(i , arr_length):
            current_sum = current_sum + arr[j]
            result = max(result , current_sum)

    return result

def maxSubArrayUsingKadane(arr):
    #store the max result found so far
    result = arr[0]

    #store the max sum of sub array ending at current position
    maxEnding = arr[0]

    for i in range(1 , len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        result = max(result , maxEnding)

    return result

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    #print(maxSumArray(arr))
    print(maxSubArrayUsingKadane(arr))
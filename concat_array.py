def concatArray(arr):
    arr_length = len(arr)
    concated_array_new = [0]*2*arr_length

    for i in range(arr_length):
        concated_array_new[i] = arr[i]
        concated_array_new[i + arr_length] = arr[i]
    return concated_array_new

if __name__ == "__main__":
    #nums = [1,2,1]
    nums = [1,3,2,1]
    concated_arr = concatArray(nums)
    for i in range(len(concated_arr)):
        print(concated_arr[i])
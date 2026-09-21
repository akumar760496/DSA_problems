def sumArray(arr):
    arr_lenght = len(arr)
    total_sum_array = 0
    sum_array_new = [0]*arr_lenght

    for i in range(arr_lenght):
        total_sum_array = total_sum_array + arr[i]
        sum_array_new[i] = total_sum_array 

    return sum_array_new

if __name__ == "__main__":
    #nums = [1,2,3,4]
    #nums = [1,1,1,1,1]
    nums = [3,1,2,10,1]
    new_arr = sumArray(nums)
    for i in range(len(new_arr)):
        print(new_arr[i])
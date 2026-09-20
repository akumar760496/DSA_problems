def reverseArray(arr):
    arr_length = len(arr)
    temp_array = [0]*arr_length

    for i in range(arr_length):
        temp_array[i] = arr[arr_length - i - 1]

    for i in range(arr_length):
        arr[i] = temp_array[i]


def reverseArrayUsingTwoPointerApproach(arr):
    lp = 0
    rp = len(arr) -1

    while(lp<rp):
        arr[lp] , arr[rp] = arr[rp] , arr[lp]
        lp = lp +1
        rp = rp -1


def rotateArrayUsingTempArray(arr,d):
    arr_length = len(arr)

    #handle the case when d > n
    d %= arr_length

    temp_array = [0]*arr_length

    for i in range(arr_length - d):
        temp_array[i] = arr[d+i]

    for i in range(d):
        temp_array[arr_length - d + i] = arr[i]

    for i in range(arr_length):
        arr[i] = temp_array[i]

if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]
    #reverseArrayUsingTwoPointerApproach(arr)
    rotateArrayUsingTempArray(arr,d=2)
    for i in range(len(arr)):
        print(arr[i])
    # reverseArray(arr)
    # for i in range(len(arr)):
    #     print(arr[i])
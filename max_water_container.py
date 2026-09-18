def maxWaterContainer(arr):
    arr_length = len(arr)
    max_water_store = 0

    for i in range(arr_length):
        for j in range(i+1, arr_length):
            container_width = j - i
            contianer_height = min(arr[i] , arr[j])
            contianer_area = contianer_height * container_width
            max_water_store = max(max_water_store, contianer_area)

    return max_water_store

def maxWaterContainerUsingTwoPointer(arr):
    arr_length = len(arr)
    max_water_store = 0
    left_pointer = 0
    right_pointer = arr_length - 1

    while(left_pointer < right_pointer):
        container_width = right_pointer - left_pointer
        container_height = min(arr[left_pointer] , arr[right_pointer])

        current_water_store = container_width * container_height
        max_water_store = max(max_water_store , current_water_store)
        if(arr[left_pointer] < arr[right_pointer]):
            left_pointer = left_pointer + 1
        else:
            right_pointer = right_pointer - 1


    

    return max_water_store




if __name__ == "__main__":
    arr = [2, 1, 8, 6, 4, 6, 5, 5]
    print(maxWaterContainerUsingTwoPointer(arr))
    #print(maxWaterContainer(arr))

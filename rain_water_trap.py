def maxWaterStored(arr):
    can_store_max_water = 0
    max_height_left = 0
    max_height_right = 0

    for i in range(1,len(arr)-1):
        #find max height on right
        max_height_right = arr[i]
        for j in range(i+1, len(arr)):
            max_height_right = max(max_height_right , arr[j])

        max_height_left = arr[i]
        for j in range(i):
            max_height_left = max(max_height_left , arr[j])

        can_store_max_water = can_store_max_water + (min(max_height_right, max_height_left) - arr[i])

    return can_store_max_water

def maxWaterTrapBetterApproach(arr):
    arr_length = len(arr)
    lmax = [0]*arr_length
    rmax = [0]*arr_length
    water_store = 0

    lmax[0] = arr[0]
    rmax[arr_length -1] = arr[arr_length -1]

    for i in range(arr_length):
        lmax[i] = max(lmax[i-1], arr[i])

    for i in range(arr_length - 2, -1, -1):
        rmax[i] = max(rmax[i+1], arr[i])

    for i in range(arr_length):
        water_store = water_store + min(lmax[i], rmax[i]) - arr[i]

    return water_store
    
    

if __name__ == "__main__":
    arr = [2, 1, 5, 3, 1, 0, 4]
    #print(maxWaterStored(arr))
    print(maxWaterTrapBetterApproach(arr))
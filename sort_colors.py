def sortColors(nums):
    num_len = len(nums)
    count0 = count1 = count2 = 0
    for i in range(num_len):
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        elif nums[i] == 2:
            count2 += 1

    idx  = 0
    for i in range(count0):
        nums[idx] = 0
        idx = idx + 1

    for i in range(count1):
        nums[idx] = 1
        idx = idx + 1

    for i in range(count2):
        nums[idx] = 2
        idx = idx + 1

    return nums

    

if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    output = sortColors(nums=nums)
    for i in range(len(output)):
        print(output[i])


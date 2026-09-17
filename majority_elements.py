def majority_elements(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        frequency = 0
        frequent_element = arr[i]
        for j in range(arr_length):
            if arr[i] == arr[j]:
                frequency = frequency + 1
                

        if frequency > (arr_length / 2):
            return frequent_element

def majority_element_using_sort(arr):
    if not arr:
        return None

    arr.sort()
    arr_length = len(arr)
    count = 1
    candidate = arr[0]

    for i in range(1, arr_length):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1
            candidate = arr[i]

        if count > arr_length // 2:
            return candidate

    return None

def majority_element_using_moore_voting(arr):
    freq = 0
    ans = 0

    for i in range(len(arr)):
        if freq == 0:
            ans = arr[i]
        if ans == arr[i]:
            freq += freq
        else:
            freq -= freq 
    return ans


if __name__ == "__main__":
    arr = [1]
    print(majority_element_using_sort(arr))




def productArray(arr):
    arr_length = len(arr)
    if arr_length < 2:
        return []

    # Initialize the product array
    product_arr = [1]*arr_length

    for i in range(arr_length):
        for j in range(arr_length):
            if i != j:
                product_arr[i]  = product_arr[i] * arr[j]
    return product_arr

def productExceptSelf(arr):
    arr_length = len(arr)
    prefProduct = [1]*arr_length
    suffixProduct = [1]*arr_length

    result = [0]*arr_length

    for i in range(1,arr_length):
        prefProduct[i] = arr[i-1]*prefProduct[i-1]

    for j in range(arr_length -2 , -1, -1):
        suffixProduct[j] = arr[j+1]*suffixProduct[j+1]

    for i in range(arr_length):
        result[i] = prefProduct[i] * suffixProduct[i]

    return result


if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    print(productArray(arr))  # Output: [24, 12, 8, 6]
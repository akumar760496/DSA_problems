def singleNumber(arr):
    if not arr:
        raise ValueError("arr must contain at least one number")
    
    result = 0
    for num in arr:
        result ^= num
    
    return result

        

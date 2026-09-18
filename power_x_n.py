def power_x_n(x,n):
    if n == 0: return 1
    if x == 0: return 0
    if x == 1: return 1
    if (x == -1 and n%2 == 0 ):return 1
    if ( x == -1 and n%2 != 0): return -1


    binary_form = n
    if n < 0:
        x = 1/x
        binary_form = - binary_form

    ans = 1
    while(binary_form > 0):
        if binary_form % 2 == 1:
            ans *= x
        x *= x
        binary_form //= 2

    return ans

if __name__ == "__main__":
    x = 2.00000
    n = -2
    print(power_x_n(x,n))
def number_pattern1():
    n = 3
    num = 1
    for i in range(n):
        for j in range(n):
            print(num, end=" ")
            num = num + 1
        # inner loop finished — move to next line
        print()

def starPattern():
    n = 4
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")

        print()

def number_pattern2():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print(i+1 , end=" ")

        print()

def character_pattern():
    # print A on first line, BB on second line
    rows = 5
    for i in range(rows):
        ch = chr(ord('A') + i)
        print(ch * (i + 1), end=" ")
        print()

def num_pattern3():
    n = 5
    for i in range(n):
        num = 1
        for j in range(i+1):
            print(num , end= " ")
            num = num +1
        print()


def num_pattern_reverse4():
    n = 5
    for i in range(n):
        num = i + 1
        for j in range(i+1):
            print(num , end=" ")
            num = num - 1
        print()

def num_floyd_pattern():
    n = 5
    num = 1
    for i in range(n):
        for j in range(i +1):
            print(num , end= " ")
            num = num + 1
        print()

def inverted_triangle_pattern():
    n = 5
    for i in range(1, n+1):
        for j in range(i-1):
            print(" ", end="")
        for j in range(n - i + 1):
            print(i , end="")
        print()

def pyramid_pattern():
    n = 5
    for i in range(1, n):
        #print space first
        for _ in range(n-i):
            print(" ", end="")

        #print num1
        for j in range(1, i+1):
            print(j, end="")

        #print num2
        for j in range(i-1,0, -1):
            print(j, end="")

        print()

def diamond_pattern():
    n = 5
    for i in range(n):

        #leading spaces
        for _ in range(n-i-1):
            print(" ", end="")
        print("*", end="")

        if( i > 0):
            for j in range(0, 2*i-1):
                print(" ", end="")
            print("*", end="")
        print()
        
    for j in range(n-1):

        print()





if __name__ == "__main__":
    #number_pattern1()
    #starPattern()
    #number_pattern2()
    #character_pattern()
    #num_pattern3()
    #num_pattern_reverse4()
    #num_floyd_pattern()
    #inverted_triangle_pattern()
    #pyramid_pattern()
    diamond_pattern()


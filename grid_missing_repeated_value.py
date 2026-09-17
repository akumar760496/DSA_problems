def find_missing_repeated_item(arr):
    un_orderedset = set()
    duplicate_element = 0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if un_orderedset.__contains__ == arr[i][j]:
                duplicate_element = arr[i][j]
            else:
                un_orderedset.add(arr[i][j])

        return duplicate_element

if __name__ == "__main__":
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    print(find_missing_repeated_item(grid))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target = 7 

def binary_search(array, target):

    left = 0
    right = len(arr) - 1

    
    while left <= right:
        # print(left, right)

        mid = (left + right) // 2

        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1


    return "Not found"


# print(binary_search(arr, 2))
print(binary_search(arr, 28))
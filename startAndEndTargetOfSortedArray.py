arr1 = [1, 3, 3, 5, 5, 5, 8, 9]; t1 = 5     # [3, 5]
arr2 = [1, 3, 3, 5, 5, 5, 8, 9]; t2 = 3     # [1, 2]
arr3 = [1, 2, 3, 4, 5, 6]; t3 = 4           # [3, 3]
arr4 = [1, 2, 3, 4, 5]; t4= 9               # [-1, -1]
arr5 = []; t5 = 3 

#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------

def binary_search(array, target):

    left = 0
    right = len(array) - 1 

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            start = mid 
            end = mid 
            left_mid = mid - 1 
            right_mid = mid + 1

            while array[left_mid] == target:
                start = left_mid 
                left_mid -= 1 

            while array[right_mid] == target:
                end = right_mid 
                right_mid += 1
            
            return [start, end]

        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1

    return [-1, -1]


print(binary_search(arr1, t1))
print(binary_search(arr2, t2))
print(binary_search(arr3, t3))
print(binary_search(arr4, t4))
print(binary_search(arr5, t5))

arr1 = [1, 3, 3, 5, 5, 5, 8, 9]; t1 = 5     # [3, 5]
arr2 = [1, 3, 3, 5, 5, 5, 8, 9]; t2 = 3     # [1, 2]
arr3 = [1, 2, 3, 4, 5, 6]; t3 = 4           # [3, 3]
arr4 = [1, 2, 3, 4, 5]; t4= 9               # [-1, -1]
arr5 = []; t5 = 3 

#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------
# BRUTE FORCE
def brute_binary_search(array, target):

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


# OPTIMAL SOLUTION
def binary_search(array, left, right, target):

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1

    return -1

def optimal_target_range(array, target):

    if len(array) == 0:
        return [-1, -1]

    first_pos = binary_search(array, 0, len(array) - 1, target)

    if first_pos == -1:
        return [-1, -1] 

    start_pos = first_pos 
    end_pos = first_pos 
    temp_left = -1 
    temp_right = -1 

    while start_pos != -1:
        temp_left = start_pos 
        start_pos = binary_search(array, 0, start_pos - 1, target)

    start_pos = temp_left 

    while end_pos != -1:
        temp_right = end_pos 
        end_pos = binary_search(array, end_pos + 1, len(array) - 1, target)

    end_pos = temp_right

    return [start_pos, end_pos]



# print(brute_binary_search(arr1, t1))
# print(brute_binary_search(arr2, t2))
# print(brute_binary_search(arr3, t3))
# print(brute_binary_search(arr4, t4))
# print(brute_binary_search(arr5, t5))
print(optimal_target_range(arr1, t1))
print(optimal_target_range(arr2, t2))
print(optimal_target_range(arr3, t3))
print(optimal_target_range(arr4, t4))
print(optimal_target_range(arr5, t5))



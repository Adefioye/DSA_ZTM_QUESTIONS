arr1 = [2, 3, 1, 2, 4, 2]; k1 = 4
arr2 = [5, 3, 1, 6, 4, 2]; k2 = 2 
arr3 = [5]; k3 = 1


#------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------

# def quick_sort(array, left, right):

#     if left < right:

#         partition_idx = partition(array, left, right)
#         quick_sort(array, left, partition_idx - 1)
#         quick_sort(array, partition_idx + 1, right)


# def partition(array, left, right):
    
#     pivot_element = array[right]
#     partition_idx = left

#     for j in range(left, len(array)):
        
#         if array[j] < pivot_element:
#             swap(array, partition_idx, j)
#             partition_idx += 1 

#     swap(array, partition_idx, right)

#     return partition_idx

# def swap(array, i, j):
#     temp = array[i]
#     array[i] = array[j]
#     array[j] = temp 

# def get_k_most_element(array, k):
#     idx_to_find = -k 
#     quick_sort(array, 0, len(array) - 1)
#     return array[idx_to_find]

# print(get_k_most_element(arr1, k1))
# print(get_k_most_element(arr2, k2))
# print(get_k_most_element(arr3, k3))

#------------------------------------------------------------------------------
# MY FIRST HOARES QUICKSELECT SOLUTION
#-------------------------------------------------------------------------------
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp 

def partition(array, left, right):

    pivot_element = array[right]
    partition_idx = left

    for j in range(left, len(array)):
        if array[j] < pivot_element:
            swap(array, partition_idx, j) 
            partition_idx += 1 

    swap(array, partition_idx, right)
        

    return partition_idx 

def quick_select(array, left, right, idx_to_find):

    print(array[left : right + 1])

    if left < right:

        partition_idx = partition(array, left, right)

        
        if (idx_to_find == partition_idx):
            print(f"Array: {array}, Index to find: {idx_to_find}, value: {array[idx_to_find]}")
            return array[idx_to_find]
        elif idx_to_find < partition_idx:
            return quick_select(array, left, partition_idx - 1, idx_to_find)
        else:
            return quick_select(array, partition_idx + 1, right, idx_to_find)


def get_k_most_element(array, k):
    idx_to_find = len(array) - k 
    quick_select(array, 0, len(array) - 1, idx_to_find)

    return array[idx_to_find]

print(get_k_most_element(arr1, k1))





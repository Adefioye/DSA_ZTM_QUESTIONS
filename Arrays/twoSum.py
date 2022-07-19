array1 = [1, 3, 7, 9, 2]
t1 = 11 
array2 = [5]
t2 = 10 

# BRUTE FORCE SOLUTION 
def two_sum(array, target):
    length = len(array)

    for i in range(length):
        number_to_find = target - array[i]

        for j in range(i+1, length):
            if j < length:
                if number_to_find == array[j]:
                    return [i, j]
    return "null"

## OPTIMAL SOLUTION using hashmap 

def two_sum_1(array, target):

    length = len(array)
    ntf_map = {} # number to find map (ntf: index)

    for i in range(length):
        current_value = array[i]

        if current_value in ntf_map:
            return [ntf_map[current_value], i]
        else:
            number_to_find = target - current_value
            ntf_map[number_to_find] = i

    return "null"

array1 = [1, 3, 7, 9, 2]
t1 = 11 

print(two_sum(array1, t1))
print(two_sum(array2, t2))

print(two_sum_1(array1, t1))
print(two_sum_1(array2, t2))




























# # BRUTE FORCE t = O(n^2) s = O(1)
# def two_sum(array, target):

#     length = len(array)
#     for l in range(length):
#         number_to_find = target - array[l]

#         for r in range(l + 1, length):
#             if r < length and array[r] == number_to_find:
#                 return [l, r]

#     return "null"

# # print(two_sum(array1, t1))
# # print(two_sum(array2, t2))


# # OPTIMAL SOLUTION t = O(n) s = O(n)
# def two_sum_1(array, target):
#     nums_map = {} # ntf : index
#     length = len(array)
#     for l in range(length):
#         current_value = array[l]

#         if current_value in nums_map:
#             return [nums_map[current_value], l]
#         else:
#             number_to_find = target - current_value
#             nums_map[number_to_find] = l
    
#     return "null"

# print(two_sum_1(array1, t1))
# print(two_sum_1(array2, t2))

# if "x" in {"x": 2}:
#     print(True)
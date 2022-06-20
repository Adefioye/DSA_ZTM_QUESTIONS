# HARD ARRAY QUESTION 
arr1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
arr2 = [3]
arr3 = []
arr4 = [3, 4, 2]
arr5 = [5, 0, 3, 0, 0, 0, 2, 3, 4, 2, 1]

# def max_trapping_water(array):
#     A = 0 
#     l = 0
#     r = l + 1 
#     min_index = 0 
#     max_index = 0 
#     array_length = len(array)

#     while r < array_length:
#         if array[r] < array[l]:
#             min_index = r 
#             r += 1 

#             if r < array_length:

#                 while array[r] <= array[min_index]:
#                     r += 1 
            
#                 max_index = r 

#                 height = min(array[l], array[max_index])
#                 width = (max_index - l - 1)

#                 A += height * width 

#                 t = max_index - 1 

#                 while t > l:
#                     A -= (array[t]) ** 2
#                     t -= 1 

#                 l = max_index 
#                 r = l + 1 
#                 # print("Inside IF")
#                 # print(l, r, A)
            
#         else:
#             l += 1 
#             r = l + 1
#             # print("Inside ELSE")
#             # print(l, r, A)

#     return A

## BRUTE FORCE SOLUTION (MY SOLUTION)

# def max_trapping_water_1(array):
#     A = 0 
#     maxL = 0
#     maxR = 0 
#     array_length = len(array)

#     for i in range(array_length):
#         l = i - 1 
#         r = i + 1 
#         if l >= 0:
#             maxL = array[l]
#         if r < array_length:
#             maxR = array[r]

#         while l >= 1:
#             if array[l - 1] > maxL:
#                 maxL = array[l - 1]
#                 l -= 1 
#             else:
#                 l -= 1 
            
#         while r < array_length - 1:
#             if array[r + 1] > maxR:
#                 maxR = array[r + 1]
#                 r += 1 
#             else:
#                 r += 1


#         result = min(maxL, maxR) - array[i] # min(maxL, maxR) - current_height

#         if result >= 0:
#             A += result 

#     return A

def max_trapping_water_2(array):

    A = 0 
    maxL = 0 
    maxR = 0 
    l = 0 
    r = len(array) - 1 
    array_length = len(array)

    while l < r:

        min_num = min(array[l], array[r])

        if min_num == array[l]:

            current_value = array[l]

            if maxL > current_value:
                A += (maxL - current_value)
                l += 1 
            else:
                maxL = current_value 
                l += 1 

        else:
            current_value = array[r]

            if maxR > current_value:
                A += (maxR - current_value)
                r -= 1 
            else:
                maxR = current_value 
                r -= 1 

    return A

print(max_trapping_water_2(arr1))
print(max_trapping_water_2(arr2))
print(max_trapping_water_2(arr3))
print(max_trapping_water_2(arr4))
print(max_trapping_water_2(arr5))




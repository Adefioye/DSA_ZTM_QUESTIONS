# HARD ARRAY QUESTION 
arr1 = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
arr2 = [3]
arr3 = []
arr4 = [3, 4, 2]

def max_trapping_water(array):
    A = 0 
    l = 0
    r = l + 1 
    min_index = 0 
    max_index = 0 
    array_length = len(array)

    while r < array_length:
        if array[r] < array[l]:
            min_index = r 
            r += 1 

            if r < array_length:

                while array[r] <= array[min_index]:
                    r += 1 
            
                max_index = r 

                height = min(array[l], array[max_index])
                width = (max_index - l - 1)

                A += height * width 

                t = max_index - 1 

                while t > l:
                    A -= (array[t]) ** 2
                    t -= 1 

                l = max_index 
                r = l + 1 
                # print("Inside IF")
                # print(l, r, A)
            
        else:
            l += 1 
            r = l + 1
            # print("Inside ELSE")
            # print(l, r, A)

    return A

print(max_trapping_water(arr1))
print(max_trapping_water(arr2))
print(max_trapping_water(arr3))
print(max_trapping_water(arr4))




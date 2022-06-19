array = [1, 8, 6, 2, 9, 4]

def container_with_most_water(array):

    maximum_area = 0
    res = [-1, -1]

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if j < len(array):
                length = min(array[j], array[i])
                breadth = j - i 
                area = length * breadth 

                if area > maximum_area:
                    maximum_area = area

    return maximum_area


# OPTIMAL SOLUTION time = O(n) space = 

def container_with_most_water_1(array):

    l = 0 
    r = len(array) - 1 
    max_area = 0 

    while l < r:

        height = min(array[l], array[r])
        width = r - l 
        area = height * width 
        max_area = max(max_area, area)

        if height == array[l]:
            l += 1 
        else:
            r -= 1

    return max_area


print(container_with_most_water(array))
print(container_with_most_water([]))
print(container_with_most_water([5]))
print(container_with_most_water([4, 5]))
print(container_with_most_water([7, 1, 2, 9]))

print(container_with_most_water_1(array))
print(container_with_most_water_1([]))
print(container_with_most_water_1([5]))
print(container_with_most_water_1([4, 5]))
print(container_with_most_water_1([7, 1, 2, 9]))
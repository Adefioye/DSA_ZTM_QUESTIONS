S1 = "abcdde"   # 4
S2 = "aaaa"     # 1 
S3 = ""         # 0 
S4 = "abcbda"   # 4 

#-------------------------------------------------------------------------------------
# MY SECOND SOLUTION (MORE CORRECT THAN THE FIRST SOLUTION)
#-------------------------------------------------------------------------------
## BRUTE FORCE SOLUTION
def brute_longest_non_repeating_substring(S):
    longest = 0 
    string_length = len(S)

    for left in range(string_length):
        seen_map = {} 
        current_length = 0

        for right in range(left, string_length):
            current_char = S[right]

            if current_char not in seen_map:
                current_length += 1 
                seen_map[current_char] = True 
                longest = max(longest, current_length) 
            else:
                break

    return longest

def optimal_longest_non_repeating_substring(S):
    longest = 0
    string_length = len(S) 
    left = 0 
    seen_map = {}

    for right in range(string_length):
        current_char = S[right]
        
        if current_char not in seen_map:
            seen_map[current_char] = right 
        else:
            prev_seen_char = seen_map[current_char]
            seen_map[current_char] = right
            
            if prev_seen_char >= left:
                left = prev_seen_char + 1 

        longest = max(longest, right - left + 1)

    return longest

print("BRUTE FORCE SOLUTION")
print(brute_longest_non_repeating_substring(S1))
print(brute_longest_non_repeating_substring(S2))
print(brute_longest_non_repeating_substring(S3))
print(brute_longest_non_repeating_substring(S4))


print("OPTIMAL SOLUTION")
print(optimal_longest_non_repeating_substring(S1))
print(optimal_longest_non_repeating_substring(S2))
print(optimal_longest_non_repeating_substring(S3))
print(optimal_longest_non_repeating_substring(S4))


#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------
## BRUTE FORCE SOLUTION

# def brute_longest_non_repeating_substring(S):
#     max_length = 0 
#     string_length = len(S)

#     for i in range(string_length):
#         char_map = {}

#         for j in range(i, string_length):
#             print(i, j, max_length)
#             current_char = S[j] 

#             if current_char not in char_map:
#                 char_map[current_char] = 1 
#             else:
#                 break 

        
#         max_length = max(max_length, len(char_map.keys()))
            

#     return max_length

# ## OPTIMAL SOLUTION

# def optimal_longest_non_repeating_substring(S):
#     string_length = len(S)
#     l = 0 
#     r = 0 
#     longest = 0 
#     seen_map = {}

#     while r < string_length:

#         current_char = S[r] 

#         if current_char not in seen_map:
#             seen_map[current_char] = r # char: index 
#             r += 1 
#         else:
#             longest = max(longest, len(seen_map.keys())) 
#             current_char_index = seen_map[current_char] 
#             l = current_char_index + 1 
#             r = l
#             seen_map = {}

#         longest = max(longest, len(seen_map.keys())) 

#     return longest


# print("BRUTE FORCE SOLUTION")
# print(brute_longest_non_repeating_substring(S4))
# print(brute_longest_non_repeating_substring(S2))
# print(brute_longest_non_repeating_substring(S3))
# print(brute_longest_non_repeating_substring(S4))

# print("OPTIMAL SOLUTION")
# print(optimal_longest_non_repeating_substring(S1))
# print(optimal_longest_non_repeating_substring(S2))
# print(optimal_longest_non_repeating_substring(S3))
# print(optimal_longest_non_repeating_substring(S4))
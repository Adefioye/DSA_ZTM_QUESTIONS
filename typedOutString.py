S1 = "ab#z" ; T1 = "az#z"       # TRUE
S2 = "abc#d" ; T2 = "acc#c"     # FALSE
S3 = "x#y#z#" ; T3 = "a#"       # TRUE 
S4 = "a###b" ; T4 = "b"         # TRUE 
S5 = "Ab#z" ; T5 = "ab#z"       # FALSE 
S6 = "abc#d" ; T6 = "abzz##d"   # TRUE
#-------------------------------------------------------------------------------------
# SECOND SOLUTION
#-------------------------------------------------------------------------------
## BRUTE FORCE SOLUTION
# time = O(a + b); space = O(a + b)
def brute_build_string(S):
    array = []
    hash = "#"

    for i in range(len(S)):
        if S[i] == hash and len(array) > 0:
            array.pop()
        else:
            array.append(S[i])
    return array 

def brute_compare_string(S, T):
    finalS = brute_build_string(S)
    finalT = brute_build_string(T)

    if len(finalS) != len(finalT):
        return False 

    for i in range(len(finalS)):
        if finalS[i] != finalT[i]:
            return False 

    return True 

## OPTIMAL SOLUTION
# time = O(a + b), space = O(1)
def back_space_compare(S, T):

    p1 = len(S) - 1 
    p2 = len(T) - 1 
    hash = "#"

    while p1 >= 0 and p2 >= 0:

        if S[p1] == hash or T[p2] == hash:

            if S[p1] == hash:
                backcount = 2 
                p1 -= 1
                backcount -= 1 
                while backcount > 0:
                    if p1 >= 0 and S[p1] == hash:
                        backcount += 2 
                    p1 -= 1
                    backcount -= 1 
            
            if T[p2] == hash:
                backcount = 2 
                p2 -= 1 
                backcount -= 1 
                while backcount > 0:
                    if p2 >= 0 and T[p2] == hash:
                        backcount += 2 
                    p2 -= 1 
                    backcount -= 1

        else:
            if S[p1] != T[p2]:
                return False 
            else:
                p1 -= 1 
                p2 -= 1 

    return True 

# print(brute_compare_string(S1, T1))
# print(brute_compare_string(S2, T2))
# print(brute_compare_string(S3, T3))
# print(brute_compare_string(S4, T4))
# print(brute_compare_string(S5, T5))
# print(brute_compare_string(S6, T6))

print(back_space_compare(S1, T1))
print(back_space_compare(S2, T2))
print(back_space_compare(S3, T3))
print(back_space_compare(S4, T4))
print(back_space_compare(S5, T5))
print(back_space_compare(S6, T6))















#-------------------------------------------------------------------------------------
# ZTM  FIRST SOLUTION
#-------------------------------------------------------------------------------
## BRUTE FORCE SOLUTION

# def build_string(string):
#     array = []
#     array_length = len(string)

#     for i in range(array_length):
#         if string[i] != "#":
#             array.append(string[i])
#         else:
#             if len(array) > 0:
#                 array.pop()

#     return array 

# def compare_string(S, T):
#     finalS = build_string(S)
#     finalT = build_string(T)

#     print(finalS, finalT)
#     if len(finalS) != len(finalT):
#         return False 
#     else:
#         for i in range(len(finalS)):
#             if finalS[i] != finalT[i]:
#                 return False
#     return True

# # print(compare_string(S1, T1))
# # print(compare_string(S2, T2))
# # print(compare_string(S3, T3))
# # print(compare_string(S4, T4))
# # print(compare_string(S5, T5))
# # print(compare_string(S6, T6))

# ## OPTIMAL SOLUTION

# def back_space_compare(S, T):
#     # Let S1 and T1 serve as POINTERS
#     p1 = len(S) - 1; p2 = len(T) - 1
#     hash = "#"

#     while p1 >= 0 or p2 >= 0:

#         if (S[p1] == hash) or (T[p2] == hash):

#             if S[p1] == hash:
#                 backcount = 2 
#                 while backcount > 0:
#                     p1 -= 1 
#                     backcount -= 1
#                     if p1 >= 0 and S[p1] == hash:
#                         backcount += 2 

#             if T[p2] == hash:
#                 backcount = 2 
#                 while backcount > 0:
#                     p2 -= 1 
#                     backcount -= 1 
#                     if p2 >= 0 and T[p2] == hash:
#                         backcount += 2 

#         else:
#             if S[p1] != T[p2]:
#                 return False 
#             else:
#                 p1 -= 1 
#                 p2 -= 1
    

#     return True

# print(back_space_compare(S1, T1))
# print(back_space_compare(S2, T2))
# print(back_space_compare(S3, T3))
# print(back_space_compare(S4, T4))
# print(back_space_compare(S5, T5))
# print(back_space_compare(S6, T6))



























#-------------------------------------------------------------------------------------
# MY SOLUTION: 
#-------------------------------------------------------------------------------
# BRUTE FORCE SOLUTION time = O(n) space = O(n)
# def typed_out_string(S, T):

#     newS = list(S)
#     newT = list(T)
#     infinity = float("-inf")

#     for i in range(len(newS)):
#         # Remove #
#         if newS[i] == "#":
#             if i - 1 < 0:
#                 newS[i] = infinity # To maintain iteration over values
#             else:
#                 newS[i] = infinity
#                 newS[i - 1] = infinity

#     for i in range(len(newT)):
#         # Remove #
#         if newT[i] == "#":
#             if i - 1 < 0:
#                 newT[i] = infinity
#             else:
#                 newT[i] = infinity
#                 newT[i - 1] = infinity 

#     # Remove infinity in both arrays
#     S_without_infinity = []
#     T_without_infinity = []

#     for i in range(len(newS)):
#         if newS[i] != infinity:
#             S_without_infinity.append(newS[i])

#     for i in range(len(newT)):
#         if newT[i] != infinity:
#             T_without_infinity.append(newT[i])

#     S = "".join(S_without_infinity)
#     T = "".join(T_without_infinity)

#     print(S, T)
#     if S == T:
#         return True 
#     else:
#         return False

## OPTIMAL SOLUTION 
# def build_string(string):
#     l = 0 
#     r = len(string) - 1

#     while r >= l:
#         if string[r] == "#":
#             oldR = r 
            
#             # 3 conditions, Either prevChar is nothing/a character/ hash
#             # If prevChar is nothing 
#             if r - 1 < 0:
#                 string = "" + string[oldR + 1:]
#                 r = len(string) - 1

#             else:
#                 # Remaining 2 conditions
#                 prevChar = string[r-1]

#                 if prevChar == "#":
#                     r -= 1

#                 else:
#                     newR = r - 2 

#                     if newR < 0:
#                         string = "" + string[oldR + 1:]
#                         r = len(string) - 1
#                     else:
#                         string = string[:newR + 1] + string[oldR + 1:]
#                         r = len(string) - 1

#         else:
#             r -= 1
        
#     return string 

# def compare_string(S, T):
#     finalS = build_string(S)
#     finalT = build_string(T)

#     print(finalS, finalT)
#     if len(finalS) != len(finalT):
#         return False 

#     else:
#         for i in range(len(finalT)):
#             if finalS[i] != finalT[i]:
#                 return False

#     return True

# print(compare_string(S1, T1))
# print(compare_string(S2, T2))
# print(compare_string(S3, T3))
# print(compare_string(S4, T4))
# print(compare_string(S5, T5))

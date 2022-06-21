S1 = "ab#z" ; T1 = "az#z"       # TRUE
S2 = "abc#d" ; T2 = "acc#c"     # FALSE
S3 = "x#y#z#" ; T3 = "a#"       # TRUE 
S4 = "a###b" ; T4 = "b"         # TRUE 
S5 = "Ab#z" ; T5 = "ab#z"       # FALSE 



def typed_out_string(S, T):
    newS = []
    newT = []

    # Remove #
    for i in range(len(S)):
        if S[i] != "#":
            newS.append(S[i])
        else:
            if len(newS) > 0:
                newS.pop()

    for i in range(len(T)):
        if T[i] != "#":
            newT.append(T[i])
        else:
            if len(newT) > 0:
                newT.pop()

    print(newS, newT)
    if len(newS) != len(newT):
        return False 
    else:
        length = len(newS)
        for i in range(length):
            if newS[i] != newT[i]:
                return False 
    
    return True







# print(typed_out_string(S1, T1))
# print(typed_out_string(S2, T2))
# print(typed_out_string(S3, T3))
# print(typed_out_string(S4, T4))
# print(typed_out_string(S5, T5))


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
def build_string(string):
    l = 0 
    r = len(string) - 1

    while r >= l:
        if string[r] == "#":
            oldR = r 
            
            # 3 conditions, Either prevChar is nothing/a character/ hash
            # If prevChar is nothing 
            if r - 1 < 0:
                string = "" + string[oldR + 1:]
                r = len(string) - 1

            else:
                # Remaining 2 conditions
                prevChar = string[r-1]

                if prevChar == "#":
                    r -= 1

                else:
                    newR = r - 2 

                    if newR < 0:
                        string = "" + string[oldR + 1:]
                        r = len(string) - 1
                    else:
                        string = string[:newR + 1] + string[oldR + 1:]
                        r = len(string) - 1

        else:
            r -= 1
        
    return string 

def compare_string(S, T):
    finalS = build_string(S)
    finalT = build_string(T)

    print(finalS, finalT)
    if len(finalS) != len(finalT):
        return False 

    else:
        for i in range(len(finalT)):
            if finalS[i] != finalT[i]:
                return False

    return True

print(compare_string(S1, T1))
print(compare_string(S2, T2))
print(compare_string(S3, T3))
print(compare_string(S4, T4))
print(compare_string(S5, T5))

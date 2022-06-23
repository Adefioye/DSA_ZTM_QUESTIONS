import math

S1 = "aabaa"                            # TRUE
S2 = "aabbaa"                           # TRUE
S3 = "abc"                              # FALSE
S4 = "a"                                # TRUE
S5 = ""                                 # FALSE
S6 = "A man, a plan, a canal: Panama"   # TRUE

# Pointer from both ends
def palindrome(S):

    newS = ""

    for i in range(len(S)):
        if S[i].isalpha() or S[i].isnumeric():
            newS += S[i]

    newS = newS.lower()

    print(newS)
    if len(newS) == 0:
        return False
    
    if len(newS) == 1:
        return True 

    l = 0 
    r = len(newS) - 1 

    while l < r:
        if newS[l] != newS[r]:
            return False 
        else:
            l += 1 
            r -= 1
    return True 

# print(palindrome(S1))
# print(palindrome(S2))
# print(palindrome(S3))
# print(palindrome(S4))
# print(palindrome(S5))
# print(palindrome(S6))

# Left and Right POINTERS from middle

def palindrome_1(S):

    newS = ""
    string_length = len(S)

    for i in range(string_length):
        if S[i].isalpha() or S[i].isnumeric():
            newS += S[i]

    newS = newS.lower()

    print(newS)
    if len(newS) == 0:
        return False
    
    if len(newS) == 1:
        return True 

    if len(newS) % 2 == 0:
        # Even
        mid = int(len(newS) / 2)
        l = mid - 1
        r = l + 1 
    else:
        mid = math.ceil(len(newS) / 2)
        l = mid - 1 
        r =  l

    while l >= 0 or r < len(newS):
        if newS[l] != newS[r]:
            return False 
        else:
            l -= 1 
            r += 1

    return True

# print(palindrome_1(S1))
# print(palindrome_1(S2))
# print(palindrome_1(S3))
# print(palindrome_1(S4))
# print(palindrome_1(S5))
# print(palindrome_1(S6))

## Reverse the string and deal with
def palindrome_2(S):

    newS = ""
    string_length = len(S)

    for i in range(string_length):
        if S[i].isalpha() or S[i].isnumeric():
            newS += S[i]

    newS = newS.lower()
    ls_newS = list(newS)
    ls_newS.reverse()
    reverse_newS = "".join(ls_newS)


    print(newS, reverse_newS)
    if len(newS) == 0:
        return False
    
    if len(newS) == 1:
        return True 

    for i in range(len(newS)):
        if newS[i] != reverse_newS[i]:
            return False 

    return True

print(palindrome_2(S1))
print(palindrome_2(S2))
print(palindrome_2(S3))
print(palindrome_2(S4))
print(palindrome_2(S5))
print(palindrome_2(S6))



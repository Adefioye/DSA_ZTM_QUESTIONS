S1 = ""         # TRUE 
S2 = "{([])}"   # TRUE
S3 = "{([]"     # FALSE 
S4 = "{[(])}"   # FALSE
S5 = "{[]()}"   # TRUE 

def valid_parentheses(S):
    parentheses = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    # print(parentheses.values())
    # print(parentheses.keys())

    string_length = len(S)
    stack = [] 

    if len(S) == 0:
        return True

    for i in range(string_length):

        current_char = S[i]

        if current_char in parentheses.values():
            stack.append(current_char)
        elif current_char in parentheses.keys():
            # Check if Stack has balancing pair 
            if len(stack) == 0:
                return False 
            elif stack[-1] != parentheses[current_char]:
                return False
            else:
                stack.pop() 


    return True if len(stack) == 0 else False 

print(valid_parentheses(S1))
print(valid_parentheses(S2))
print(valid_parentheses(S3))
print(valid_parentheses(S4))
print(valid_parentheses(S5))
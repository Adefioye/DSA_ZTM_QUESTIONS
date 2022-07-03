S1 = "a)bc(d)"
S2 = "(ab(c)d" 
S3 = "))(("

#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------

def min_brackets_remove(S):
    string_length = len(S)
    stack = []
    open_bracket = "("
    close_bracket = ")"
    no_open_bracket = 0

    for i in range(string_length):
        current_char = S[i]

        if current_char == open_bracket:
            stack.append(current_char)
            no_open_bracket += 1
        elif current_char == close_bracket:
            if open_bracket in stack:
                stack.append(current_char)
                no_open_bracket -= 1 
        else:
            stack.append(current_char)

    
    while no_open_bracket != 0:
        if open_bracket in stack:
            index = stack.index(open_bracket)
            stack.pop(index)
            no_open_bracket -= 1
                
            
    return "".join(stack)

print(min_brackets_remove(S1))
print(min_brackets_remove(S2))
print(min_brackets_remove(S3))
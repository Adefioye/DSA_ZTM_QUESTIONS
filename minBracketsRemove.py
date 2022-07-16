S1 = "a)bc(d)"
S2 = "(ab(c)d" 
S3 = "))(("





#-------------------------------------------------------------------------------------
# MY SECOND SOLUTION
#---------------------------------------------------------------------------
# SOLUTION 1
def remove_min_brackets(S):
    stack_open = []
    stack_close = []
    string_list = list(S)
    inf = "inf"

    for i in range(len(S)):
        current_char = S[i]

        if current_char == "(":
            stack_open.append(i) 
        elif current_char == ")":

            if len(stack_open) > 0:
                stack_open.pop()
            else:
                stack_close.append(i)

    
    while len(stack_open) > 0:
        idx = stack_open.pop()
        string_list[idx] = inf 
    
    while len(stack_close) > 0:
        idx = stack_close.pop()
        string_list[idx] = inf 

    while inf in string_list:
        idx = string_list.index(inf)
        string_list.pop(idx)
        
    return "".join(string_list)

print(remove_min_brackets(S1))
print(remove_min_brackets(S2))
print(remove_min_brackets(S3))

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

# print(min_brackets_remove(S1))
# print(min_brackets_remove(S2))
# print(min_brackets_remove(S3))
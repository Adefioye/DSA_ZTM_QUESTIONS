def brute_cycle_detection(head):

    current_node = head 
    my_set = set() 

    while(current_node.value not in my_set):
        if current_node.next == None:
            return False 

        my_set.add(current_node.value)
        current_node = current_node.next

    return current_node


# Optimal solution is based on tortoise and hare algorithm 
def optimal_cycle_detection(head):

    hare = head 
    tortoise = head 

    while True:
        hare = head.next
        tortoise = head.next 

        if hare == None or hare.next == None:
            return False 
        else:
            hare = hare.next 

        if hare == tortoise:
            break

    p1 = head 
    p2 = hare 

    while p1 != p2:
        
        p1 = p1.next 
        p2 = p2.next 

    return p1
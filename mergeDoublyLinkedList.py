#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------
def flatten_list(head):
    current_node = head 

    while current_node:
        if current_node.child == None:
            current_node = current_node.next
        else:
            child_tail_node = current_node.child 

            while child_tail_node.next != None:
                child_tail_node = child_tail_node.next

            current_node.next = current_node.child 
            current_node.next.prev = current_node 
            child_tail_node.next = current_node.next 
            if child_tail_node.next.prev != None:
                child_tail_node.next.prev = child_tail_node

            current_node.child = None

    return head
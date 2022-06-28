#-------------------------------------------------------------------------------------
# MY FIRST SOLUTION
#-------------------------------------------------------------------------------

class node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.length = 0

class linked_list:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0 

    def print(self, linkedlist):
        value_array = []
        current_value = linkedlist
        while current_value:
            value_array.append(current_value.value) 
            current_value = current_value.next 

        return value_array

    def push(self, value):
        new_node = node(value)

        if self.head == None:
            self.head = new_node 
            self.tail = self.head 

        self.tail.next = new_node 
        self.tail = new_node
        self.length += 1 

    def reverse(self, head):
        current_node = head 
        self.tail = head 
        prev_node = None 

        while current_node:
            next_node = current_node.next 
            current_node.next = prev_node 
            prev_node = current_node 
            current_node = next_node 

        self.head = prev_node 

        return [self.head, self.tail] 

    def m_n_reversal(self, m, n):
        # 1) Grab leadernode of m node
        # 2) Get a reference to m node and traverse to n node 
        # 3) Get reference to follower node of n node 
        # 4) Reverse m to n node and return head and tail 
        # 5) Point leader node in #1 to head in #4 
        # 6) Point tail in #4 to follower node in #3 

        if self.head.value == m and self.tail.value == n:
            self.reverse(self.head)

        else:
            # Get leadernode of m
            # Get follower node of n 
            # Run steo #5 and #6 
            m_leader_node = None 
            n_follower_node = None
            m_node = None

            nodes_before_m = self.head 
            previous_node = self.head
            next_node = previous_node.next 

            while next_node:
                if next_node.value == m:
                    m_leader_node = previous_node 
                    m_leader_node.next = None
                    m_node = next_node
                    break

                previous_node = next_node
                next_node = next_node.next
                    

            # Grab follower node of n node 
            print(self.print(nodes_before_m))
            m_temp_node = m_node 
            while m_temp_node:
                if m_temp_node.value == n:
                    n_follower_node = m_temp_node.next 
                    n_node = m_temp_node
                    n_node.next = None # Since n node is now the tail 
                    break

                m_temp_node = m_temp_node.next 

            # Get head and tail of m to n list 
            m_n_head, m_n_tail = self.reverse(m_node)

            # Point m leader node to head 
            # print(self.print(m_leader_node.next))
            # print(self.print(n_follower_node))
            # print(self.print(m_n_head))
            # print(self.print(m_n_tail))
            temp_nodes_before_m = nodes_before_m
            while temp_nodes_before_m:
                if temp_nodes_before_m.next == None:
                    temp_nodes_before_m.next = m_n_head
                    break

                temp_nodes_before_m = temp_nodes_before_m.next
                print(self.print(temp_nodes_before_m)) 

            m_n_tail.next = n_follower_node

            # Set head to m leader node
            self.head = nodes_before_m

        return self.head 


linked_list = linked_list()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)
linked_list.push(6)
linked_list.push(7)
linked_list.push(8)
linked_list.push(9)
linked_list.push(10)
print(linked_list.print(linked_list.head))
# linked_list.m_n_reversal(1, 5)
# print(linked_list.print(linked_list.head))
linked_list.m_n_reversal(2, 7)
print(linked_list.print(linked_list.head))





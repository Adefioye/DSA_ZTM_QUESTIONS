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

    def push(self, value):
        new_node = node(value)

        if self.head == None:
            self.head = new_node 
            self.tail = self.head 

        self.tail.next = new_node 
        self.tail = new_node
        self.length += 1 

    def reverse(self):

        current_node = self.head 
        prev_node = None 
        self.tail = self.head

        while current_node:
            next_node = current_node.next 
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node 

    def print(self):
        current_node = self.head 

        while current_node:
            print(current_node.value)
            current_node = current_node.next 


linked_list = linked_list()
linked_list.push(5)
linked_list.push(8)
linked_list.push(7)
linked_list.reverse()
linked_list.print()



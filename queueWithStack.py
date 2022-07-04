class queue_with_stack:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):

        if (len(self.stack_out) == 0):
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop() 

    def peek(self):

        if (len(self.stack_out) == 0):
            self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def empty(self):
        return len(self.stack_in) == 0 and len(self.stack_out) == 0 



queue_with_stack = queue_with_stack()

print(queue_with_stack.empty())
queue_with_stack.enqueue(1)
queue_with_stack.enqueue(2)
queue_with_stack.enqueue(3)
queue_with_stack.enqueue(4)
queue_with_stack.enqueue(5)
print(queue_with_stack.stack_in)
queue_with_stack.dequeue()
queue_with_stack.dequeue()
print(queue_with_stack.stack_in)
print(queue_with_stack.peek())
print(queue_with_stack.empty())


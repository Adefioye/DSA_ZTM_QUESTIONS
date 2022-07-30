from math import floor

class priority_queue:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.heap[0]

    def __parent(self, idx):
        parent_idx = floor((idx - 1) / 2)
        return parent_idx

    def __left_child(self, idx):
        left_child_idx = (2 * idx) + 1
        return left_child_idx

    def __right_child(self, idx):
        right_child_idx = (2 * idx) + 2
        return right_child_idx

    def __is_greater_comparator(self, a, b):
        return a > b 

    def __swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def insert(self, data):
        data_idx = self.size()
        self.heap.insert(data_idx, data) 
        parent_idx = self.__parent(data_idx)
        parent_data = self.heap[parent_idx]

        while parent_idx >= 0 and data > parent_data:
            self.__swap(data_idx, parent_idx)
            data_idx = parent_idx
            parent_idx = self.__parent(data_idx)
            parent_data = self.heap[parent_idx]

        return self.heap
    
    def remove(self):
        
        if len(self.heap) > 0:
            self.heap.pop(0)

        self.heap.insert(0, self.heap.pop(len(self.heap) - 1))

        parent_data = self.heap[0]
        parent_data_idx = 0
        
        left_idx, right_idx, left_data, right_data = self.__get_left_and_right_child(0)
        max_data = max(left_data, right_data)

        while max_data > parent_data:

            if max_data == left_data:
                max_data_idx = left_idx
            else:
                max_data_idx = right_idx

            self.__swap(max_data_idx, parent_data_idx)

            parent_data_idx = max_data_idx
            parent_data = self.heap[parent_data_idx]
            left_idx, right_idx, left_data, right_data = self.__get_left_and_right_child(parent_data_idx)
            max_data = max(left_data, right_data)

        return self.heap

    def __get_left_and_right_child(self, idx):
        left_idx = self.__left_child(idx)
        right_idx = self.__right_child(idx)

        try:
            left_data = self.heap[left_idx]
        except:
            left_data = float("-inf")

        try:
            right_data = self.heap[right_idx]
        except:
            right_data = float("-inf")

        return [left_idx, right_idx, left_data, right_data]



prq = priority_queue()

prq.heap = [50, 40, 25, 20, 35, 10, 15]

# print(prq.heap)
prq.insert(45)
prq.insert(75)

print(prq.remove())
print(prq.remove())


class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def insert(self, data):
        new_node = Node(data, self._head)
        self._head = new_node
        self._size+=1
    
    def get_list(self):
        result = []
        pointer = self._head
        while pointer != None:
            result.append(pointer.data)
            pointer = pointer.next_node

        return result
    
    def __len__(self):
        return self._size

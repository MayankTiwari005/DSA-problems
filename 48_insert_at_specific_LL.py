class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class singleLL:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.val is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def insert_at(self, val, position):     # time complexity: O(N), space complexity: O(1)
        new_node = Node(val)
        if position == 0:
            new_node = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:      # position is where the node needs to be inserted
                prev_node = current
                current = current.next
                count += 1
            prev_node.next = new_node
            new_node.next = current
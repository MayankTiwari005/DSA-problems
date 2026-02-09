# append, traverse, delete, traverse
class node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class singlyLinkedList:
    # Time complexity: O(N), Space complexity: O(1)
    def __init__(self):
        self.head = None
    # before append there are two cases:
    def append(self, val):
        new_node = node(val)   # append(5) will give: new_node -> |5 | None|
        if self.head == None:  # 1. if SLL is empty i.e, head has NONE value
            self.head = new_node    
        else:   # 2. SLL is not empty
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def traversal(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ")
                curr = curr.next
            print()
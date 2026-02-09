# leetcode 206

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node 
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def traverse(self):
        if self.head is None:
            print(" empty ")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ")
                curr = curr.next
            print()

    def add_in(self, val, position):        # position where the node needs to be inserted
        new_node = Node(val)        # node object creation, say it having a address on 117 inside the disk
        if position == 0:           # inserting at head
            new_node == self.head
            self.head == new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current.next = current
                count += 1
            prev_node.next = new_node       # address play
            new_node.next = current

# time complexity: O(N + N/2)
# space complexity: O(1)
    def brute(self, val):
        temp = self.head
        stack =[]
        while temp is not None:
            stack.append(temp.val)
        
        temp = self.head
        while temp is not None:
            e = stack.pop
            temp.val = e
            temp = temp.next
        return self.head

sll = SingleLinkedList()    #object creation
sll.traverse()      # empty
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.traverse()  # list
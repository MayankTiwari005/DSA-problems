
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class doubly_LL:
    def __init__(self):
        self.head = None
    
    def append_head(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while self.head is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
    
    def append_at_pos(self, data, pos):
        new_node = Node(data)
        if pos == self.head:
            self.append_head(data)
            return
        
        temp = self.head
        count = 0
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print("outer bound")
            return
        
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node


    # TIME COMPLEXITY: O(2N) ~ O(N)
    # SPACE COMPLEXITY: O(N)
    def brute_stack(self, val):
        temp=self.head
        stack = []
        while self is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = self.head
        while self is not None:
            e = stack.pop()
            temp.val = e
            temp = temp.next
        return self.head
    
    def optimal(self,val):
        if self.head is None:
            return self.head
        curr = self.head
        prev = None
        while curr is not None:
            front = curr.next
            curr.next = prev
            curr.prev = front
            prev = curr
            curr = curr.next
        return self.prev
    
# Leetcode 328

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
    
    def brute(self):
        if self.head is None or self.head.next is None:
            return self.head
        temp = self.head
        values = []
        while temp is not None:
            values.append(temp.val)
            temp.next.next
        
        temp = self.head.next
        while temp is not None:
            values.append(temp.val)
            temp.next.next
        
        temp = self.head
        idx = 0
        while temp is not None:
            temp.val = values[idx]
            temp.next
        return self.head
    
    def optimal(self):

        if self.head is None or self.head.next is None:
            return self.head
        
        even_head = self.head.next
        odd = self.head
        even = self.head.next

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
        
        odd.next = even_head
        return self.head

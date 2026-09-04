

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class doubly_LL:
    def __init__(self):
        self.head = None
    
    def del_occuracnce(self, val, key):
        if self.head is None and self.head.val== key:
            return None
        temp = self.head
        prev = None
        new_head = self.head
        
        while temp is not None:
            if temp.val == key:

                if prev is not None:
                    prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next

            prev = temp
            temp = temp.next
        return new_head
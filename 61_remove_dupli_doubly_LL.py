
'''
1 <=> 2 <=> 3 <=> 3 <=> 4 <=> 6 <=> 6     : should look like -> 1 <=> 2 <=> 3 <=> 4 <=> 6

1 <=> 1 <=> 1 <=> 2 <=> 3 <=> 3    : should look like: 1 <=> 2 <=> 3
'''



class doubly_LL:
    def __init__(self):
        self.head = None
    
    def del_duplpicates_doubly_ll(self, data):
        if self.head is None:
            return None
        curr = self.head
        prev = None
        
        while curr.next is not None:
            if curr.prev.data == self.head.data:
                curr.prev = self.head
            
            if curr.prev.data == curr.data:
                curr.prev.prev.next = curr
                curr.prev = curr.prev.prev
            
            curr = curr.next
            
        return self.head
    
        def removeDuplicates(self, head):
            if head is None:
                return head
            curr = head

            while curr and curr.next:
                if curr.data == curr.next.data:
                    curr.next = curr.next.next
                    if curr.next:
                        curr.next.prev = curr
                else:
                    curr = curr.next

            return self.head
    
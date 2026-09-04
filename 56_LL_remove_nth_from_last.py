# leetcode 19

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
    
    def brute(self, n):
        # O(N) time
        # O(2N) space
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        if length == n:
            new_head = self.head.next
            # del head
            return new_head
        pos = length - n
        temp = self.head
        count = 1
        while count < pos:
            temp = temp.next
            count += 1
        temp.next = temp.next.next
        return self.head
    
    def optimal(self, n):
        # time O(N)
        # space O(1)
        slow = self.head
        fast = self.head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return self.head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow = slow.next.next
        return self.head
    
# leetcode 142

# leetcode 141

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
    
    def cyclic_brute(self):
        temp = self.head
        my_set = set()
        while temp is not None:
            if temp in my_set:
                return temp
            else:
                my_set.add(temp)
                temp = temp.next
        return None
    
    def cyclic_optimal(self):
        slow = self.head
        fast = fast.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
    
    def cyclic(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
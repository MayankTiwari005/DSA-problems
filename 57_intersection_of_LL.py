# leetcoe 160

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
   
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        temp_a = headA
        temp_b = headB
        while temp_a != temp_b:

            if temp_a is not None:
                temp_a = temp_a.next
            else:
                temp_a = headB
            if temp_b is not None:
                temp_b = temp_b.next
            else:
                temp_b = headA
        
        return temp_a    
# length of cycle if formed

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

    def length_cycle_brute(self):
        temp = self.head
        my_dict = dict()
        travel = 0
        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
                        
            my_dict[temp] = travel
            travel += 1
            temp = temp.next

    def length_optimal(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
    

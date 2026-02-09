"""
while temp stores the temprory valur of self.head
when self.head is moved and temp.next->None in this cases python automatically detects that the temp not not pointing to anywhere,
so it automatically delets the node after some time from memory
there is 1 more option for manual deletion that is "del" keyword, we can write del temp, it deletes the temp node
"""


class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class singleLL:
    def __init(self):
        self.head = None
    
    def append(self, data):
        new_node = node(data)
        if self.val is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr.next = curr
            curr.next = new_node
    def traverse(self):
        if self.head is None:
            print(" EMPTY LINKED LIST")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end = " ")
                curr.next = curr
            print()

    def add_node(self, val, position):
        new_node = node(val)
        if position == 0:
            new_node = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current.next = current
                count += 1
            prev_node.next = new_node
            new_node.next = current
    
    def delete_node(self, val):     # value is the thing that needs to be deleted
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                del temp
                # OR temp.next = None
                return
            else:
                found = False       # value to be deleted checker, to know if value does even exist that needs to be deleted
                prev = None
                while temp is not None:
                    if temp == val:
                        found = True
                        break       # value caught, true the found and came out of while loop 
                    prev = temp
                    temp = temp.next
                
                if found:
                    prev.next = temp.next
                    del temp
                    # or temp.next = None
                else:
                    print("node not found")
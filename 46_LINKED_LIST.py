'''
linked list work on node value:
where each node has 2 values -> data and next address
'''
class node:
    def __init__(self, val):
        self.val = val
        self.next = None

node1 = node(5)
node2 = node(10)
node3 = node(7)
node4 = node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print(node1)    #give some random address from storage
print(node2)    #another random adddress from storage

print(node1.val)
print(node1.next)
print(f"{node2.val} is same as {node1.next.val}")
print(f"node4 value by the use of node1 is: {node1.next.next.next.val}") 
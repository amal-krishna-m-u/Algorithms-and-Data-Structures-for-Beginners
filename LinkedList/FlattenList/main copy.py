class Node:
    def __init__(self, val, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def FlattenList(Head):
    if not Head:
        return None
    
    dummy = Node(0)  
    curr = dummy 
    
    def dfs(node):
        nonlocal curr  
        if not node:
            return
        
        new_node = Node(node.val)
        curr.next = new_node  
        curr = new_node  
        if node.child:
            dfs(node.child)
        
        if node.next:
            dfs(node.next)

    dfs(Head)  
    return dummy.next  

# Constructing the multilevel linked list
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node11 = Node(11)
node12 = Node(12)
node13 = Node(13)
node14 = Node(14)
node15 = Node(15)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node7.next = node8
node8.next = node9
node9.next = node10
node11.next = node12
node12.next = node13
node14.next = node15

node3.child = node7
node8.child = node11
node12.child = node14

# Flatten and print
new_head = FlattenList(head)

while new_head:
    print(new_head.val, "->", end=" ")
    new_head = new_head.next

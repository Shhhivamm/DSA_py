class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at(self,val,position):
        new_node = node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            
            while curr is not None and count < position:
                prev_node = curr
                curr = curr.next
                count += 1
            prev_node.next = new_node
            new_node.next = curr
    def traverse(self):
        if not self.head:
            print("LL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end="-->" )
                curr = curr.next
            print()

ll = LinkedList()
ll.insert_at(10,0)
ll.insert_at(100,2)
ll.insert_at(5,1)
ll.insert_at(40,3)
ll.insert_at(50,4)
ll.traverse()
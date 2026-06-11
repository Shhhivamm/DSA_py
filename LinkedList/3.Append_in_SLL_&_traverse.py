class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self,val):
        new_node = node(val)
        if self.head == None:  #LL is empty
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            
    def traverse(self):
        if not self.head:
            print("Linked list is empty")
        else:
            curr =self.head
            while curr is not None:
                print(curr.val, end="-->")
                curr = curr.next             
            print()
            
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.traverse()

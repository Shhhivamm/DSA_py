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
    def delete(self,val):
        curr = self.head
        if curr.next is not None:
            if curr.val == val:    
                # self.head = curr.next
                self.head = curr.next
                del curr
                return
            else:
                found = False   # by this we check if the node exist or not
                prev = None
                
                while curr is not None:
                    if curr.val == val:
                        found = True
                        break
                    prev = curr
                    curr = curr.next
                if found:
                    prev.next = curr.next
                    del curr
                    return 
                else:
                    print("Node not found")
                    
ll = LinkedList()
ll.insert_at(5,0)
ll.insert_at(10,1)
ll.insert_at(21,2)
ll.insert_at(17,3)
ll.insert_at(3,4)
ll.traverse()

ll.delete(5)
ll.traverse()
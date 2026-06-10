
#node class
class Node:
    def __init__(self,data= None, next = None):
        self.data = data
        self.next = next
        
#Linked list class
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
        
ll = Linkedlist()

ll.insert_at_beginning(5)
ll.insert_at_beginning(10)
ll.insert_at_beginning(15)
ll.insert_at_beginning(20)
ll.insert_at_beginning(25)
ll.insert_at_beginning(30)
ll.insert_at_beginning(35)
ll.print()
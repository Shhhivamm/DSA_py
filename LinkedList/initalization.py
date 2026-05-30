#node class
class Node:
    def __init__(self,data= None, next = None):
        self.data = data
        self.next = next
        
#Linked list class
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def instet_at_begining(self,data):
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
        
if __name__ == '__main__':
    ll = Linkedlist()
    ll.instet_at_begining(5)
    ll.instet_at_begining(10)
    ll.instet_at_begining(15)
    ll.instet_at_begining(20)
    ll.print()
        
        

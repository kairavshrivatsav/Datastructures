class Node():
    def __init__(self, value, next=None):
        self.next = next
        self.value = value
    
class LinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail=self.head
        self.length=0
    

    def tail_insert(self, value):
        if self.length==0:
            self.head.value=value
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        self.length+=1
        
    def head_insert(self,value):
        old_head=self.head
        self.head=Node(value)
        self.head.next=old_head

    def __str__(self):
        elements=""
        current = self.head
        while current:
            elements+=str(current.value)+"->"
            current = current.next
        elements+="None"
        return elements

    def search(self, element):
        current=self.head
        index=0
        while current:
            
            if current.value==element:
                return index
            else:
                index+=1
                current=current.next
        return -1

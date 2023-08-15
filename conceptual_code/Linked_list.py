

class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None
    
    
class Linked_list:
    def __init__(self) -> None:
        self.head=None
        
    def deleted_at_position(self,pos):
        if pos==0:
            delnode=self.head
            self.head=delnode.next
            del delnode
        else:
            temp=self.head
            for i in range(pos-2):
                temp=temp.next
                if temp==None:
                    print('Out of boundary')
                    return
                
            delNode=temp.next
            temp.next=temp.next.next
            del delNode
    
    def insert_at_position(self,pos,val):
        newNode=Node(val)
        if pos==0:
            newNode.next=self.head
            self.head=newNode
        
        else:
            temp=self.head
            for i in range(pos-2):
                temp=temp.next
                if temp==None:
                    print('Out of boundary')
                    return
            newNode.next=temp.next
            temp.next=newNode
    
    def insert_at_tail(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
            
    def print_list(self):
        temp=self.head
        while temp!=None:
            print(temp.val , end=" ")
            temp=temp.next
            
    def reverse(self):
        if self.head.next==None:
            return self.head
        save=self.head
        self.head=self.head.next
        newHead=self.reverse()
        save.next.next=save
        save.next=None
        return newHead
        
def main():
    lst=Linked_list()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.insert_at_tail(40)
    lst.print_list()
    print()
    lst.insert_at_position(4,100)
    lst.print_list()
    print()
    lst.deleted_at_position(0)
    lst.print_list()
    print()
    lst.head=lst.reverse()
    lst.print_list()
    
    
main()
    
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
            return
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
            newNode.prev=curr
            
    def delete(self,val):
        if not self.head:
            print("list is empty")
            return
        curr=self.head
        while curr is not None:
            if curr.val==val:
                if curr.prev==None:
                    self.head=curr.next
                    if self.head:
                        self.head.prev=None
                else:
                    curr.prev.next=curr.next
                    if curr.next:
                        curr.next.prev=curr.prev
                return

    def printList(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print('None')
dll=doublyLinkedList()
dll.append(1)
dll.append(2)
dll.delete(1)
dll.printList()
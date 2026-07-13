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
    def insert(self,val,position):
        newNode=Node(val)
        if position==0:
            newNode.next=self.head
            if self.head:
                self.head.prev=newNode
            self.head=newNode
            return
        curr=self.head
        count=0
        while curr.next is not None and count<position-1:
            curr=curr.next
            count+=1
        newNode.next=curr.next
        newNode.prev=curr
        if curr.next is not None:
            curr.next=newNode
        curr.next=newNode
    def delete(self,k):
        temp=self.head
        while temp:
            if temp.val==k:
                if temp.prev==None:
                    self.head=temp.next
                    if self.head:
                        self.head.prev=None
                else:
                    temp.prev.next=temp.next
                    if temp.next:
                        temp.next.prev=temp.prev
                return
            temp=temp.next
    def printList(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print('None')
dll=doublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
dll.delete(2)
dll.printList()
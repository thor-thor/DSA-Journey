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

    def printList(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print('None')
dll=doublyLinkedList()
dll.append(1)
dll.append(2)
dll.insert(3,1)
dll.printList()
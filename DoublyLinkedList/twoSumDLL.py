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
    def twoSum(self,target):
        temp1=self.head
        result=[]
        while temp1 is not None:
            temp2=temp1.next
            while temp2 is not None:
                if temp1.val+temp2.val==target:
                    result.append([temp1.val,temp2.val])
                temp2=temp2.next
            temp1=temp1.next
        return result
    def printList(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print('None')
dll=doublyLinkedList()
dll.append(0)
dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)
print(dll.twoSum(4))
dll.printList()
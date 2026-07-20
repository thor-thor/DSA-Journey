class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class MyQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def push(self,item):
        newNode=Node(item)
        if self.rear is None:
            self.front=self.rear=newNode
            return
        self.rear.next=newNode
        self.rear=newNode
    def pop(self):
        if self.front is None:
            return -1
        popped=self.front.data
        self.front=self.front.next

        if self.front is None:
            self.rear=None
        return popped
    def printList(self):
        curr=self.front
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("None")
sll=MyQueue()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.pop()
sll.printList()
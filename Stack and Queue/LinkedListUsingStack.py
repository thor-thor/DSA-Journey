class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class MyStack:
    def __init__(self):
        self.top=None
    def append(self,data):
        newNode=Node(data)
        newNode.next=self.top
        self.top=newNode
    def pop(self):
        if self.top is None:
            return -1
        popped=self.top.data
        self.top=self.top.next
        return popped
    def printStack(self):
        curr=self.top
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("Npone")
sll=MyStack()
sll.append(10)
sll.append(20)
sll.append(30)
sll.pop()
sll.printStack()
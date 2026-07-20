class QueueUsingStack:
    def __init__(self):
        self.st1=[]
        self.st2=[]
    def push(self,items):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(items)
        while self.st2:
            self.st1.append(self.st2.pop())
    def pop(self):
        if not self.st1:
            return "queue is empty"
        topElement=self.st1.pop()
        return topElement
    def peek(self):
        if not self.st1:
            return "stack is empty"
        return self.st1[-1]
    def empty(self):
        return len(self.st1)==0
stack=QueueUsingStack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.st1)
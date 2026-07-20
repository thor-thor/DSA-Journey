from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.items=deque()
    def append(self,item):
        self.items.append(item)
        for _ in range(len(self.items)-1):
            self.items.append(self.items.popleft())
    def pop(self):
        if len(self.items)==0:
            return "satck is empty"
        return self.items.popleft()
    def peek(self):
        if len(self.items)==0:
            return "stack is empty"
        return self.items[0]
    def size(self):
        return len(self.items)==0
queue=StackUsingQueue()
queue.append(10)
queue.append(60)
queue.append(90)
queue.append(50)
queue.append(40)
print(queue.items)
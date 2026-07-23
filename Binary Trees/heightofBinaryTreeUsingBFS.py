from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
drinks=Node('drinks')
hot=Node('hot')
cold=Node('cold')
tea=Node('tea')
coffe=Node('coffe')
cola=Node('cola')
sprite=Node('sprite')
drinks.left=hot
drinks.right=cold
hot.left=tea
hot.right=coffe
cold.left=cola
cold.right=sprite
def heightNode(node):
    
    queue=deque([])
    height=0
    queue.append(node)
    while len(queue)!=0:
        levelSize=len(queue)
        height+=1
        for _ in range(levelSize):
            e=queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height
print(heightNode(drinks))
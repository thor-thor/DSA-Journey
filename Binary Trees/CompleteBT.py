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
class Solution:
    def completeBT(self,node):
        if not node:
            return True
        queue=deque([node])
        isFound=False
        while queue:
            node=queue.popleft()
            if node is None:
                isFound=True
            else:
                if isFound:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
obj=Solution()
print(obj.completeBT(drinks))
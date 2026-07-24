class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

class Solution:
    def __init__(self):
        self.maxi=float("-inf")
    def findMaxPathSum(self,root):
        if not root:
            return 0
        leftPathSum=self.findMaxPathSum(root.left)
        rightPathSum=self.findMaxPathSum(root.right)
        if leftPathSum<0:
            leftPathSum=0
        if rightPathSum<0:
            rightPathSum=0
        self.maxi=max(self.maxi,leftPathSum+root.val+rightPathSum)
        return max(leftPathSum,rightPathSum)+root.val
    def maxPathSum(self,node):
        self.findMaxPathSum(node)
        return self.maxi
obj=Solution()
print(obj.maxPathSum(root))